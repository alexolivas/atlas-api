from django.http import Http404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from web.models import AboutInfo
from web.serializers.about_info_serializer import AboutInfoSerializer


class AboutInfo(APIView):
    """
    This endpoint returns the "about info" to display on the about section of the website
    """
    permission_classes = (AllowAny,)

    @staticmethod
    def get_about_info():
        try:
            return AboutInfo.objects.all()[0]
        except:
            return None

    def get(self, request, format=None):
        about_info = AboutInfoSerializer(self.get_about_info())
        return Response(about_info.data, status=status.HTTP_200_OK)
