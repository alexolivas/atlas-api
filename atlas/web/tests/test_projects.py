from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory

from atlas.projects.models import Project
from atlas.web.models import TechnicalSkill
from atlas.web.views.projects_views import ListFeaturedProjects, ListProjects, ProjectDetails


class ListProjectsViewEmptyTest(TestCase):
    """ This test suite runs tests against the list projects endpoint
    without any existing projects in the database """

    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()
        cls.view = ListProjects.as_view()

    def setUp(self):
        Project.objects.all().delete()

    def test_get_endpoint(self):
        """ This test verifies the GET endpoint returns a 200 without any records
        since there aren't any in the database """
        request = ListProjectsViewEmptyTest.factory.get('/web/projects/')
        response = ListProjectsViewEmptyTest.view(request)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals([], response.data)


class ListProjectsViewTest(TestCase):
    """ This test suite runs tests against the list projects endpoint,
    creating a few test projects, and verifying logic around GET and filtering """

    @classmethod
    def setUpClass(cls):
        num = Project.objects.all()
        cls.factory = APIRequestFactory()
        cls.view = ListProjects.as_view()
        cls.featured_view = ListFeaturedProjects.as_view()

        cls.project_1 = Project.objects.create(
            name='Test Project 1',
            production_url='www.alexolivas.com',
            repo_url='git@somerepo.git',
            tech_stack_display='python + postgres',
            description='lorem ipsum',
            technology_description='lorem ipsum',
            public_repo=True,
            display_on_website=True
        )
        cls.project_2 = Project.objects.create(
            name='Test Project 2',
            production_url='www.alexolivas.com',
            repo_url='git@somerepo.git',
            tech_stack_display='python + postgres',
            description='lorem ipsum',
            technology_description='lorem ipsum',
            public_repo=True,
            display_on_website=True
        )
        cls.project_3 = Project.objects.create(
            name='Test Project 3',
            production_url='www.alexolivas.com',
            repo_url='git@somerepo.git',
            tech_stack_display='python + postgres',
            description='lorem ipsum',
            technology_description='lorem ipsum',
            public_repo=True,
            display_on_website=True
        )

        cls.featured_project_1 = Project.objects.create(
            name='Featured Project 1',
            production_url='www.alexolivas.com',
            repo_url='git@somerepo.git',
            tech_stack_display='python + postgres',
            description='lorem ipsum',
            technology_description='lorem ipsum',
            public_repo=True,
            display_on_website=True,
            featured_project=True
        )
        cls.featured_project_2 = Project.objects.create(
            name='Featured Project 2',
            production_url='www.alexolivas.com',
            repo_url='git@somerepo.git',
            tech_stack_display='python + postgres',
            description='lorem ipsum',
            technology_description='lorem ipsum',
            public_repo=True,
            display_on_website=True,
            featured_project=True
        )
        cls.featured_project_3 = Project.objects.create(
            name='Featured Project 3',
            production_url='www.alexolivas.com',
            repo_url='git@somerepo.git',
            tech_stack_display='python + postgres',
            description='lorem ipsum',
            technology_description='lorem ipsum',
            public_repo=True,
            display_on_website=True,
            featured_project=True
        )
        cls.featured_project_4 = Project.objects.create(
            name='Featured Project 4',
            production_url='www.alexolivas.com',
            repo_url='git@somerepo.git',
            tech_stack_display='python + postgres',
            description='lorem ipsum',
            technology_description='lorem ipsum',
            public_repo=True,
            display_on_website=True,
            featured_project=True
        )

        cls.hidden_project = Project.objects.create(
            name='Hidden Project',
            production_url='www.alexolivas.com',
            repo_url='git@somerepo.git',
            tech_stack_display='python + postgres',
            description='lorem ipsum',
            technology_description='lorem ipsum',
            public_repo=True,
            display_on_website=False
        )

        cls.expected_projects = [
            cls.project_1.id,
            cls.project_2.id,
            cls.project_3.id,
            cls.featured_project_1.id,
            cls.featured_project_2.id,
            cls.featured_project_3.id,
            cls.featured_project_4.id
        ]

        cls.expected_featured_projects = [
            cls.featured_project_1.id,
            cls.featured_project_2.id,
            cls.featured_project_3.id,
            cls.featured_project_4.id
        ]

    @classmethod
    def tearDownClass(cls):
        Project.objects.all().delete()
        num = Project.objects.all()

    def test_get_endpoint(self):
        """ This test verifies the GET endpoint returns the complete list of active projects """
        request = ListProjectsViewTest.factory.get('/web/projects/')
        response = ListProjectsViewTest.view(request)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(self.expected_projects), len(response.data))

    def test_get_featured_projects(self):
        """ This test verifies the GET endpoint only returns 3 featured projects """
        request = ListProjectsViewTest.factory.get('/web/projects/featured/')
        response = ListProjectsViewTest.featured_view(request=request)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(3, len(response.data))
        for project in response.data:
            self.assertIn(project['id'], self.expected_featured_projects)

    def test_get_projects_with_limit_param(self):
        """ This test verifies the GET endpoint only return the number of projects set by the limit param """
        request = ListProjectsViewTest.factory.get('/web/projects/?limit=2')
        response = ListProjectsViewTest.view(request)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(2, len(response.data))

    def test_get_projects_invalid_limit_param(self):
        """ This test verifies the GET endpoint returns an error message when a GET param is invalid """
        request = ListProjectsViewTest.factory.get('/web/projects/?limit=d')
        response = ListProjectsViewTest.view(request)
        self.assertEquals(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEquals('Limit must be a number', response.data['detail'])

        request = ListProjectsViewTest.factory.get('/web/projects/?limit=101')
        response = ListProjectsViewTest.view(request)
        self.assertEquals(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEquals('Limit must be a number between 1 and 100', response.data['detail'])

        request = ListProjectsViewTest.factory.get('/web/projects/?limit=0')
        response = ListProjectsViewTest.view(request)
        self.assertEquals(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEquals('Limit must be a number between 1 and 100', response.data['detail'])

        request = ListProjectsViewTest.factory.get('/web/projects/?limit=-1')
        response = ListProjectsViewTest.view(request)
        self.assertEquals(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEquals('Limit must be a number', response.data['detail'])


class ProjectDetailsViewTest(TestCase):
    """ This test suite runs tests against the project details view """
    @classmethod
    def setUpClass(cls):
        cls.factory = APIRequestFactory()
        cls.view = ProjectDetails.as_view()

        python_skill = TechnicalSkill.objects.create(
            name='Python',
            skill_type=TechnicalSkill.PROGRAMMING_LANGUAGE,
            description='sample'
        )

        cls.test_project = Project.objects.create(
            name='Test Project',
            production_url='www.alexolivas.com',
            repo_url='git@somerepo.git',
            tech_stack_display='python + postgres',
            description='this project is one that I want to show off on my website',
            technology_description='lorem ipsum',
            public_repo=True,
            display_on_website=True
        )
        cls.test_project.technology.set([python_skill])
        cls.test_project.save()

        # # Add a screen shot for this photo
        # cls.test_project_photo = ProjectPhoto.objects.create(
        #     url='some/url/',
        #     project=cls.test_project
        # )

        cls.hidden_project = Project.objects.create(
            name='Test Hidden Project',
            production_url='www.alexolivas.com',
            repo_url='git@somerepo.git',
            tech_stack_display='python + postgres',
            description='this project should not appear on my website, it exists for my personal tracking',
            technology_description='lorem ipsum',
            public_repo=False,
            display_on_website=False
        )

    @classmethod
    def tearDownClass(cls):
        Project.objects.all().delete()
        TechnicalSkill.objects.all().delete()

    def test_get_project(self):
        """ This test verifies the GET endpoint returns a project's details  """
        request = ProjectDetailsViewTest.factory.get('/web/projects/{0}'.format(self.test_project.id))
        response = ProjectDetailsViewTest.view(request, project_id=self.test_project.id)

        # Verify all 10 expected fields are returned in the response, spot check some of them
        # to verify this is the project we are expecting
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(11, len(response.data))
        self.assertEquals(self.test_project.id, response.data['id'])
        self.assertEquals(self.test_project.name, response.data['name'])
        self.assertEquals(self.test_project.production_url, response.data['production_url'])
        self.assertEquals(self.test_project.description, response.data['description'])
        # self.assertEquals(1, len(response.data['photos']))

        # Verify the rest of the expected fields are in the response
        self.assertTrue('repo_url' in response.data)
        self.assertTrue('tech_stack_display' in response.data)
        self.assertTrue('technology_description' in response.data)
        self.assertTrue('public_repo' in response.data)
        self.assertTrue('technology' in response.data)
        self.assertTrue('photos' in response.data)
        self.assertTrue('main_photo' in response.data)

    def test_get_invalid_project(self):
        """ This test verifies the GET endpoint returns a 404 for a non-existent project """
        request = ProjectDetailsViewTest.factory.get('/web/projects/200')
        response = ProjectDetailsViewTest.view(request, project_id=200)
        self.assertEquals(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertEquals('Project not found', response.data['detail'])

    def test_get_invalid_request(self):
        """ This test verifies the GET endpoint returns a 404 for an invalid request """
        request = ProjectDetailsViewTest.factory.get('/web/projects/a')
        response = ProjectDetailsViewTest.view(request, project_id='a')
        self.assertEquals(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEquals('Invalid project ID, expecting a number', response.data['detail'])

    def test_get_private_project(self):
        """ This test verifies the GET endpoint returns a 404 for a project that exists but is
        not marked for public access e.g. not viewable on the website """
        request = ProjectDetailsViewTest.factory.get('/web/projects/{0}'.format(self.hidden_project.id))
        response = ProjectDetailsViewTest.view(request, project_id=self.hidden_project.id)
        self.assertEquals(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertEquals('Project not found', response.data['detail'])
