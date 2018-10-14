import git

from django.conf import settings

from rest_framework.response import Response
from rest_framework.views import APIView


class AtlasAPIVersion(APIView):
    """ This endpoint returns this project's (Atlas API) current version depending on the
    environment that it is running on.
    * Development: version = {latest commit hash}-{branch name}
    * Stage: version = latest tag pointing to the development branch
    * Production: version = latest tag pointing to the production branch
    """

    def get(self, request):
        # https://gitversion.readthedocs.io/en/latest/git-branching-strategies/gitflow-examples/
        print("*** inside atlas api version GET method ***")
        # TODO see https://stackoverflow.com/questions/3760086/automatic-tagging-of-releases (Look at answer with 22)
        # https://gitversion.readthedocs.io/en/latest/more-info/version-increments/ (use gitVersion for atlas)
        # TODO for the react-app
        # https://github.com/facebook/create-react-app/issues/1917 << use this to increment that version after commit
        # https://github.com/facebook/create-react-app/issues/2486
        # https://github.com/facebook/create-react-app/issues/2466 << use this to read version from package.json

        environment = settings.ENVIRONMENT
        # release_lifecycle = '' if environment == 'production' else ('-dev'
        # if environment == 'development' else '-beta')

        # import subprocess
        # tag = subprocess.check_output(["git", "describe", "--always"]).strip()
        # repo = git.Repo(search_parent_directories=True)
        repo = git.Repo()
        # if development, get the current latest commit hash
        # tag = repo.head.object.hexsha

        # TODO: MASTER release and master will be the same on heroku, I will heroku promote stage to prod
        # TODO: RELEASE branch will be deployed to my live stage server
        # TODO: DEVELOP branches will be ignored, only tests will be run
        # TODO: FEATURE branches will be ignored, only tests will be run

        # By default,
        tag = repo.head.object.hexsha
        print("hexsha: {0}".format(repo.head.object.hexsha))
        print("binsha: {0}".format(repo.head.object.binsha))
        print("repo: {0}".format(repo.head.object.repo))
        print("active_branch: {0}".format(repo.active_branch))
        print("tags: {0}".format(repo.tags))
        print(repo.tags[0])
        print("Tag commit: {0}".format(repo.tags[0].commit))

        # TODO https://coderwall.com/p/mk18zq/automatic-git-version-tagging-for-npm-modules
        tag = None
        if environment == 'production':
            # Get the latest tag on the master branch, verify the last commit matches the tag
            tag = repo.tags[0]
            version = tag
        elif environment == 'stage':
            tag = repo.tags[0]
            version = tag
        elif environment == 'development':
            # Finally, if the user is running a development version of
            # the Atlas API just get the latest commit hash
            tag = str(repo.head.object.hexsha)[:10]
            active_branch = repo.active_branch.name[:25]
            version = '{0}-{1}'.format(tag, active_branch)

        print(repo.heads)

        for branch in repo.branches:
            print("Branch name: {0}".format(branch))
            print("Latest commit on this branch: {0}".format(str(branch.commit.hexsha)[:10]))
            print(" ")

        # if tag is None:
        #     raise Http500

        # if stage, get the current tag on the develop branch
        # if production, get the latest tag on the master branch
        # tag = '0.0.1'
        # version = '{0}{1}'.format(str(tag), release_lifecycle)

        # Reach out to the endpoint
        return Response({
            'version': version
        })
