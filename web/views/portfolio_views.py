from django.http import Http404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from projects.models import Project
from web.serializers.portfolio_serializer import PortfolioSerializer


class ListFeaturedProjects(ListAPIView):
    """
    This endpoint returns a list of 3 featured projects in random order
    """
    permission_classes = (AllowAny,)
    queryset = Project.objects.filter(display_on_website=True, featured_project=True).order_by('?')[:3]
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        return self.queryset


class ListProjects(ListAPIView):
    """
    This endpoint returns a list of projects selected to be viewed on my portfolio website
    """
    permission_classes = (AllowAny,)
    queryset = Project.objects.filter(display_on_website=True)
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        return self.queryset


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
        project = PortfolioSerializer(self.get_project(pk))
        return Response(project.data, status=status.HTTP_200_OK)
