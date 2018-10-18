import atlas

from unittest import mock

from django.conf import settings
from django.contrib.auth.models import User, Group
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from rest_framework.authtoken.models import Token

from atlas.web.views.atlas_views import AtlasAPIVersion


class AtlasVersionTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()
        cls.view = AtlasAPIVersion.as_view()

        cls.user = User.objects.create_user(
            'test',
            'test@test.com',
            'test',
        )
        Token.objects.get_or_create(user=cls.user)
        cls.group = Group(name='Web Clients')
        cls.group.save()

        cls.user.groups.add(cls.group)
        cls.user.save()

    @mock.patch('git.Repo')
    def test_on_development_environment_feature_branch(self, mock_repo):
        """ User is running development environment and on a feature branch """
        with self.settings(ENVIRONMENT='development'):
            mock_active_branch_name = 'feature/unit-testing-sample'[:25]
            mock_active_branch = mock.MagicMock()
            mock_active_branch.name = mock_active_branch_name
            mock_repo.return_value = mock.MagicMock(active_branch=mock_active_branch)

            request = AtlasVersionTest.factory.get('/web/version/')
            force_authenticate(request, user=self.user, token=self.user.auth_token)

            response = AtlasVersionTest.view(request)

            expected_version = '{0}-dev.{1}'.format(atlas.VERSION, mock_active_branch_name)
            self.assertEquals(status.HTTP_200_OK, response.status_code)
            self.assertEquals(expected_version, response.data['version'])

    @mock.patch('git.Repo')
    def test_on_development_environment_develop_branch(self, mock_repo):
        """ User is running development environment and on the develop branch """
        with self.settings(ENVIRONMENT='development'):
            mock_active_branch_name = 'develop'
            mock_active_branch = mock.MagicMock()
            mock_active_branch.name = mock_active_branch_name

            mock_latest_commit_sha = '128196c3a9234ac13c23'[:10]
            mock_head_object = mock.MagicMock()
            mock_head_object.hexsha = mock_latest_commit_sha
            mock_repo.return_value = mock.MagicMock(
                active_branch=mock_active_branch,
                head=mock.MagicMock(object=mock_head_object)
            )

            request = AtlasVersionTest.factory.get('/web/version/')
            force_authenticate(request, user=self.user, token=self.user.auth_token)

            response = AtlasVersionTest.view(request)

            # The latest commit SHA is used rather than the branch name on develop
            expected_version = '{0}-dev.{1}'.format(atlas.VERSION, mock_latest_commit_sha)
            self.assertEquals(status.HTTP_200_OK, response.status_code)
            self.assertEquals(expected_version, response.data['version'])

    @mock.patch('git.Repo')
    def test_on_development_environment_release_branch(self, mock_repo):
        """ User is running development environment and on a release branch """
        with self.settings(ENVIRONMENT='development'):
            mock_active_branch_name = 'release/{0}'.format(atlas.VERSION)
            mock_active_branch = mock.MagicMock()
            mock_active_branch.name = mock_active_branch_name

            mock_latest_commit_sha = '128196c3a9234ac13c23'[:10]
            mock_head_object = mock.MagicMock()
            mock_head_object.hexsha = mock_latest_commit_sha
            mock_repo.return_value = mock.MagicMock(
                active_branch=mock_active_branch,
                head=mock.MagicMock(object=mock_head_object)
            )

            request = AtlasVersionTest.factory.get('/web/version/')
            force_authenticate(request, user=self.user, token=self.user.auth_token)

            response = AtlasVersionTest.view(request)

            # The latest commit SHA is used rather than the branch name on release (when in local development)
            expected_version = '{0}-dev.{1}'.format(atlas.VERSION, mock_latest_commit_sha)
            self.assertEquals(status.HTTP_200_OK, response.status_code)
            self.assertEquals(expected_version, response.data['version'])

    @mock.patch('git.Repo')
    def test_on_development_environment_master_branch(self, mock_repo):
        """ User is running development environment and on the master branch """
        with self.settings(ENVIRONMENT='development'):
            mock_active_branch_name = 'master'
            mock_active_branch = mock.MagicMock()
            mock_active_branch.name = mock_active_branch_name

            mock_latest_commit_sha = '128196c3a9234ac13c23'[:10]
            mock_head_object = mock.MagicMock()
            mock_head_object.hexsha = mock_latest_commit_sha
            mock_repo.return_value = mock.MagicMock(
                active_branch=mock_active_branch,
                head=mock.MagicMock(object=mock_head_object)
            )

            request = AtlasVersionTest.factory.get('/web/version/')
            force_authenticate(request, user=self.user, token=self.user.auth_token)

            response = AtlasVersionTest.view(request)

            # The latest commit SHA is used rather than the branch name on master (when in local development)
            expected_version = '{0}-dev.{1}'.format(atlas.VERSION, mock_latest_commit_sha)
            self.assertEquals(status.HTTP_200_OK, response.status_code)
            self.assertEquals(expected_version, response.data['version'])

    @mock.patch('git.Repo')
    def test_on_stage_environment(self, mock_repo):
        """ User is running a staging environment """
        with self.settings(ENVIRONMENT='stage'):
            mock_active_branch_name = 'release/{0}'.format(atlas.VERSION)
            mock_active_branch = mock.MagicMock()
            mock_active_branch.name = mock_active_branch_name

            mock_latest_commit_sha = '128196c3a9234ac13c23'[:10]
            mock_head_object = mock.MagicMock()
            mock_head_object.hexsha = mock_latest_commit_sha
            mock_repo.return_value = mock.MagicMock(
                active_branch=mock_active_branch,
                head=mock.MagicMock(object=mock_head_object)
            )

            request = AtlasVersionTest.factory.get('/web/version/')
            force_authenticate(request, user=self.user, token=self.user.auth_token)

            response = AtlasVersionTest.view(request)

            # The latest commit SHA is used on a stage build
            expected_version = '{0}-rc.{1}'.format(atlas.VERSION, mock_latest_commit_sha)
            self.assertEquals(status.HTTP_200_OK, response.status_code)
            self.assertEquals(expected_version, response.data['version'])

    @mock.patch('git.Repo')
    def test_on_production_environment(self, mock_repo):
        """ User is running a production environment """

        # Note: if the environment variable is omitted, then the environment is assumed to be
        # production
        with self.settings(ENVIRONMENT=None):
            mock_active_branch_name = 'master'
            mock_active_branch = mock.MagicMock()
            mock_active_branch.name = mock_active_branch_name
            mock_repo.return_value = mock.MagicMock(active_branch=mock_active_branch)

            request = AtlasVersionTest.factory.get('/web/version/')
            force_authenticate(request, user=self.user, token=self.user.auth_token)

            response = AtlasVersionTest.view(request)

            # On production simply show the version
            self.assertEquals(status.HTTP_200_OK, response.status_code)
            self.assertEquals(atlas.VERSION, response.data['version'])