# from django.http import Http404
# from rest_framework import status
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from web.models import Expertise
# from web.serializers.expertise_serializer import ExpertiseSerializer
#
#
# class ExpertiseDetails(APIView):
#     """
#     This endpoint returns my technical expertise details
#     """
#     permission_classes = (AllowAny,)
#
#     def get(self, request, format=None):
#         """
#         Return of a list of technical expertise
#         :param request:
#         :param format:
#         :return: JSON object array containing expertise details
#         """
#         expertise = Expertise.objects.all()
#         expertise_serializer = ExpertiseSerializer(expertise, many=True)
#         return Response(expertise_serializer.data, status=status.HTTP_200_OK)
