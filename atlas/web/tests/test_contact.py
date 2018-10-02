from unittest import mock

from django.core import mail
from django.test import SimpleTestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory

from atlas.web.views.contact_views import ContactMe


class ContactMeTest(SimpleTestCase):
    """ This test suite verifies the contact me endpoint """

    factory = APIRequestFactory()
    view = ContactMe.as_view()

    def setUp(self):
        # Reset the outbox after every test
        mail.outbox = []

    def test_successful_email_request(self):
        """ This test verifies the behavior of a successful email request """
        data = {
            'name': 'Django User',
            'subject': 'I am sending an email',
            'from': 'django.user@testing.com',
            'message': 'Hello, this is an email'
        }
        request = ContactMeTest.factory.post('/web/contact/', data)
        response = ContactMeTest.view(request)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'I am sending an email')
        self.assertEqual(mail.outbox[0].from_email, 'django.user@testing.com')

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals('Message sent!', response.data['details'])
        self.assertEquals(True, response.data['success'])

    @mock.patch('atlas.web.views.contact_views.send_mail')
    def test_error_email_request(self, mocked_send_mail):
        """ This test verifies the endpoint's robust behavior if it encounters
        an external error sending an email """

        # mocked_send_mail = mock.Mock(side_effect=Exception('Boom!'))
        mocked_send_mail.side_effect = Exception('Any random error')
        data = {
            'name': 'Django User',
            'subject': 'I am sending an email',
            'from': 'django.user@testing.com',
            'message': 'Hello, this is an email'
        }
        request = ContactMeTest.factory.post('/web/contact/', data)
        response = ContactMeTest.view(request)

        self.assertTrue(mocked_send_mail.called)
        self.assertEquals(status.HTTP_500_INTERNAL_SERVER_ERROR, response.status_code)
        self.assertEquals('Any random error', response.data['details'])
        self.assertEquals(False, response.data['success'])

    def test_form_validation(self):
        """ This test verifies the endpoint fails unless all the expected
        fields are validated """
        data = {
        }
        request = ContactMeTest.factory.post('/web/contact/', data)
        response = ContactMeTest.view(request)

        self.assertEquals(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertTrue('details' in response.data)
        expected_form_errors = [
            'Name is required',
            'Subject is required',
            'Email is required',
            'Message body is required'
        ]
        for error_message in response.data['details']:
            self.assertTrue(error_message in expected_form_errors)

        # Add a couple fields but still let the endpoint produce a validation error
        data = {
            'name': 'Django User',
            'subject': 'I am sending you an email'
        }
        request = ContactMeTest.factory.post('/web/contact/', data)
        response = ContactMeTest.view(request)

        self.assertEquals(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertTrue('details' in response.data)
        expected_form_errors = [
            'Email is required',
            'Message body is required'
        ]
        for error_message in response.data['details']:
            self.assertTrue(error_message in expected_form_errors)

    def test_throttling(self):
        pass

    def test_get_request_fails(self):
        """ This test verifies that a 405 is returned if a GET is attempted on this endpoint """
        request = ContactMeTest.factory.get('/web/contact/')
        response = ContactMeTest.view(request)

        self.assertEqual(len(mail.outbox), 0)
        self.assertEquals(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)
