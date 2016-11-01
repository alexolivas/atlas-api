from django.http import Http404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from projects.models import Project
from projects.serializers.public.project_detail_serializer import ProjectDetailSerializer


class AboutInfo(APIView):
    """
    This endpoint returns the "about info" to display on the about section of the website
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
