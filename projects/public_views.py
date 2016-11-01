from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView
from models import Project
from serializers.public_project_serializer import PublicProjectSerializer


class ListProjects(APIView):
    """
    This endpoint returns a list of projects selected to be viewed on my portfolio website
    """
    throttle_classes = (AnonRateThrottle,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        """
        Return of a list of all active projects selected to appear on my portfolio website
        :param request:
        :param format:
        :return: JSON object array containing project details
        """
        projects = Project.objects.filter(display_on_website=True)
        projects_serializer = PublicProjectSerializer(projects, many=True)
        return Response(projects_serializer.data, status=status.HTTP_200_OK)
