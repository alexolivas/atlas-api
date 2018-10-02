# from django.test import TestCase
#
# from rest_framework import status
# from rest_framework.test import APIRequestFactory
#
# from atlas.projects.models import Project
# from atlas.projects.views import ListProjects
#
#
# class ListProjectsViewEmptyTest(TestCase):
#     """ This test suite runs tests against the list projects endpoint
#     without any existing projects in the database """
#
#     @classmethod
#     def setUpClass(cls):
#         cls.factory = APIRequestFactory()
#         cls.view = ListProjects.as_view()
#
#     def setUpTestData(self):
#         pass
#
#     @classmethod
#     def tearDownClass(cls):
#         Project.objects.all().delete()
#
#     def test_get_endpoint(self):
#         """ This test verifies the GET endpoint returns a 200 without any records
#         since there aren't any in the database """
#         request = ListProjectsViewEmptyTest.factory.get('/web/projects/')
#         response = ListProjectsViewEmptyTest.view(request)
#         print(response)
#         self.assertEquals(status.HTTP_200_OK, response.status_code)
#         self.assertEquals({}, response.data)
#
#
# class ListProjectsViewTest(TestCase):
#     """ This test suite runs tests against the list projects endpoint,
#     creating a few test projects, and verifying logic around GET and filtering """
#
#     @classmethod
#     def setUpClass(cls):
#         cls.factory = APIRequestFactory()
#         cls.view = ListProjects.as_view()
#
#     def setUpTestData(self):
#         # Then create a few mock projects to test the API's projects endpoint
#         pass
#
#     @classmethod
#     def tearDownClass(cls):
#         Project.objects.all().delete()
#
#     def test_get_endpoint(self):
#         """ This test verifies the GET endpoint return the complete list of projects """
#         pass
#
#     def test_get_featured_projects(self):
#         """ This test verifies the GET endpoint to return featured projects successfully
#         returns only featured projects """
#         pass
#
#     def test_get_featured_projects_for_home_page(self):
#         """ This test verifies the GET endpoint to return featured projects successfully
#         returns only featured 3 projects """
#         pass
#
#     def test_get_endpoint_with_filter(self):
#         """ Implement this test once filtering is added (there should be several types of this
#         test depending on the fields we are allowing to use for filtering) """
#         pass
