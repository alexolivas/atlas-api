import git

from django.conf import settings

from rest_framework.response import Response
from rest_framework.views import APIView

import atlas


class AtlasAPIVersion(APIView):
    """ This endpoint returns this project's (Atlas API) current version """

    def get(self, request):
        repo = git.Repo()
        version = atlas.__version__

        if settings.ENVIRONMENT == 'stage':
            hexsha = str(repo.head.object.hexsha)[:10]
            version = '{0}-rc.{1}'.format(version, hexsha)
        elif settings.ENVIRONMENT == 'development':
            # The development environment will show the current version plus the branch name, unless
            # that branch is develop, release, or master
            active_branch = str(repo.active_branch.name)[:25]

            on_develop = active_branch.startswith('develop')
            on_release = active_branch.startswith('release/')
            on_master = active_branch.startswith('master')
            if on_develop or on_release or on_master:
                # The user is not on a feature or hotfix branch, in this case the version displayed
                # is based on the sha of the latest commit rather than the branch name
                active_branch = str(repo.head.object.hexsha)[:10]
            version = '{0}-dev.{1}'.format(version, active_branch)

        return Response({
            'version': version
        })
