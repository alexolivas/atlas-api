from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from atlas.web.models import CareerSnapshot
from atlas.web.serializers.career_snapshot_serializer import CareerSnapshotSerializer


class ResumeTimeline(APIView):
    """
    This endpoint returns my resume: career highlights such as jobs or promotions
    """
    permission_classes = (AllowAny,)

    # @staticmethod
    # def get_resume():
    #     try:
    #         return Project.objects.get(pk=pk, display_on_website=True)
    #     except Project.DoesNotExist:
    #         raise Http404

    def get(self, request, format=None):
        """
        Return of a list of my career highlights
        :param request:
        :param format:
        :return: JSON object array containing project details
        """
        resume = CareerSnapshot.objects.filter(active=True).order_by('-year', '-month')
        career_snapshot_serializer = CareerSnapshotSerializer(resume, many=True)
        return Response(career_snapshot_serializer.data, status=status.HTTP_200_OK)
