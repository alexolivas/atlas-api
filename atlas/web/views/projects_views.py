from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from atlas.projects.models import Project
from atlas.web.permissions import WebsiteAccessPermission
from atlas.web.serializers.project_serializer import ProjectSerializer


class ListFeaturedProjects(ListAPIView):
    """
    This endpoint returns a list of 3 featured projects in random order
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly, WebsiteAccessPermission)
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all()
        queryset = queryset.filter(display_on_website=True, featured_project=True).order_by('?')[:3]
        return queryset


class ListProjects(ListAPIView):
    """
    This endpoint returns a list of projects selected to be viewed on my portfolio website
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly, WebsiteAccessPermission)
    serializer_class = ProjectSerializer

    def list(self, request):
        """
        Optionally restricts the projects by whether they are featured or not
        """
        queryset = Project.objects.all()

        # Validate the limit GET parameter, it should be a number between 1 and 100
        limit = self.request.query_params.get('limit', None)
        if limit and not limit.isdigit():
            return Response({
                'detail': 'Limit must be a number'
            }, status=status.HTTP_400_BAD_REQUEST)
        elif limit and limit.isdigit():
            if 0 < int(limit) <= 100:
                serializer = ProjectSerializer(queryset.filter(display_on_website=True)[:int(limit)], many=True)
                return Response(serializer.data)
            else:
                return Response({
                    'detail': 'Limit must be a number between 1 and 100'
                }, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProjectSerializer(queryset.filter(display_on_website=True), many=True)
        return Response(serializer.data)


class ProjectDetails(APIView):
    """
    This endpoint returns a project's details
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly, WebsiteAccessPermission)

    def get(self, request, project_id, format=None):
        try:
            project = Project.objects.get(id=project_id, display_on_website=True)
            serializer = ProjectSerializer(project)
            return Response(serializer.data)
        except Project.DoesNotExist:
            return Response({'detail': 'Project not found'}, status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({'detail': 'Invalid project ID, expecting a number'}, status.HTTP_400_BAD_REQUEST)
