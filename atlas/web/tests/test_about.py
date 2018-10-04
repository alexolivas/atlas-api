from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from rest_framework.authtoken.models import Token

from atlas.web.models import AboutInfo
from atlas.web.views.about_views import AboutDetails


class AboutInfoViewsTest(TestCase):
    """ This test suite runs tests against the about details endpoint """

    @classmethod
    def setUpClass(cls):
        cls.factory = APIRequestFactory()
        cls.view = AboutDetails.as_view()
        cls.user = User.objects.create_user(
            'test',
            'test@test.com',
            'test',
        )
        Token.objects.get_or_create(user=cls.user)

    def setUp(self):
        # Delete all about info objects before every test
        AboutInfo.objects.all().delete()

    @classmethod
    def tearDownClass(cls):
        AboutInfo.objects.all().delete()
        User.objects.all().delete()

    def test_empty_about_info_request(self):
        """ This test verifies that the endpoint returns successfully without any about info records """

        request = AboutInfoViewsTest.factory.get('/web/about-info/')
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        response = AboutInfoViewsTest.view(request)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals({}, response.data)

    def test_successful_home_request(self):
        """ This test verifies the about info endpoint for the home page """

        # Create the about info object for the home page
        AboutInfo.objects.create(
            description='Lorem ipsum description for the home page',
            location='home'
        )

        # Verify that the home about info object is returned when no GET param is
        # passed in as it is the default
        request = AboutInfoViewsTest.factory.get('/web/about-info/')
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        response = AboutInfoViewsTest.view(request)
        expected_response = {
            'location': 'home',
            'profile_photo': None,
            'description': 'Lorem ipsum description for the home page'
        }
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(expected_response, response.data)

        # Now explicitly pass in the GET param and verify the same response is returned
        request = AboutInfoViewsTest.factory.get('/web/about-info/?location=home')
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        response = AboutInfoViewsTest.view(request)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(expected_response, response.data)

    def test_successful_about_request(self):
        """ This test verifies the about info endpoint for the about page """

        # Create the about info object for the about page
        AboutInfo.objects.create(
            description='Lorem ipsum description for the about page',
            location='about'
        )

        # Verify that the home about info object is returned when no GET param is
        # passed in as it is the default
        request = AboutInfoViewsTest.factory.get('/web/about-info/?location=about')
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        response = AboutInfoViewsTest.view(request)
        expected_response = {
            'location': 'about',
            'profile_photo': None,
            'description': 'Lorem ipsum description for the about page'
        }
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(expected_response, response.data)

    def test_unauthenticated_about_info_request(self):
        """ This test verifies that the endpoint fails with unauthenticated requests """

        request = AboutInfoViewsTest.factory.get('/web/about-info/')
        response = AboutInfoViewsTest.view(request)
        self.assertEquals(status.HTTP_401_UNAUTHORIZED, response.status_code)

        request = AboutInfoViewsTest.factory.get('/web/about-info/?location=home')
        response = AboutInfoViewsTest.view(request)
        self.assertEquals(status.HTTP_401_UNAUTHORIZED, response.status_code)

        request = AboutInfoViewsTest.factory.get('/web/about-info/?location=about')
        response = AboutInfoViewsTest.view(request)
        self.assertEquals(status.HTTP_401_UNAUTHORIZED, response.status_code)


class AboutInfoModelTest(TestCase):
    """ This test suite verifies model restrictions """

    def setUp(self):
        # Clear the database
        AboutInfo.objects.all().delete()

    def test_only_one_instance_per_location(self):
        """ This test verifies that we can only create one about info object per location """

        # Create the about info object for the home page
        about_info = AboutInfo.objects.create(
            description='Lorem ipsum description for the home page',
            location='home'
        )
        self.assertEquals(about_info.id, 1)

        # Create the about info object for the about page
        home_info = AboutInfo.objects.create(
            description='Lorem ipsum description for the about page',
            location='about'
        )
        self.assertEquals(home_info.id, 2)

        try:
            # Create the about info object for the home page
            AboutInfo.objects.create(
                description='Lorem ipsum description for the home page',
                location='home'
            )
            self.fail("We should not be able to create more than one info object where the location is home")
        except IntegrityError as e:
            # self.assertContains(str(e), "duplicate key value violates unique constraint")
            pass
