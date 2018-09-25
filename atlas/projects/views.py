from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from atlas.projects.models import Project
from atlas.projects.serializers.project_serializer import ProjectSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

# from atlas.projects.filters import ProjectFilter


class ListProjects(ListAPIView):
    """
    This endpoint returns a list of projects selected to be viewed on my portfolio website
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    # filter_class = ProjectFilter
    search_fields = ('name',)
    ordering_fields = ('name', 'account')

    def get_queryset(self):
        return self.queryset


class ProjectDetails(APIView):
    """
    This endpoint returns a project's details
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdminUser)

    @staticmethod
    def get_project(pk):
        # NOTE: I need to create a project utils class to help with the different types of queries
        try:
            return Project.objects.get(pk=pk, display_on_website=True)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Returns the details of a specific project
        :param request:
        :param pk:
        :param format:
        :return:
        """
        project = ProjectSerializer(self.get_project(pk))
        return Response(project.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """
        Creates a new project
        :param request:
        :param format:
        :return:
        """
        pass

    def patch(self, request, pk, format=None):
        """
        Updates an existing project by passing in only the changed attributes
        :param request:
        :param pk:
        :param format:
        :return:
        """
        pass

    def delete(self, request, pk, format=None):
        """
        Deletes an existing project (marks it as deleted)
        :param request:
        :param pk:
        :param format:
        :return:
        """
        pass
