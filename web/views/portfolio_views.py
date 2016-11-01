from django.http import Http404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from projects.models import Project
from web.serializers.project_detail_serializer import ProjectDetailSerializer
from web.serializers.projects_serializer import ProjectsSerializer


class ListProjects(APIView):
    """
    This endpoint returns a list of projects selected to be viewed on my portfolio website
    """
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        """
        Return of a list of all active projects selected to appear on my portfolio website
        :param request:
        :param format:
        :return: JSON object array containing project details
        """
        projects = Project.objects.filter(display_on_website=True)
        projects_serializer = ProjectsSerializer(projects, many=True)
        return Response(projects_serializer.data, status=status.HTTP_200_OK)


class ProjectDetails(APIView):
    """
    This endpoint returns a project's details
    """
    permission_classes = (AllowAny,)

    @staticmethod
    def get_project(pk):
        try:
            return Project.objects.get(pk=pk, display_on_website=True)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = ProjectDetailSerializer(self.get_project(pk))
        return Response(project.data, status=status.HTTP_200_OK)
