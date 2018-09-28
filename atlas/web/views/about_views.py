from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from atlas.web.models import AboutInfo
from atlas.web.models import Expertise
from atlas.web.models import TechnicalSkill
from atlas.web.serializers.about_info_serializer import AboutInfoSerializer
from atlas.web.serializers.technology_serializer import TechnicalSkillSerializer

from atlas.web.serializers.expertise_serializer import ExpertiseSerializer


class AboutDetails(APIView):
    """
    This endpoint returns the "about details"
    """
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        queryset = AboutInfo.objects.all()
        location = self.request.query_params.get('location', AboutInfo.HOME)
        queryset = queryset.filter(location=location)[0]
        about_info = AboutInfoSerializer(queryset)
        return Response(about_info.data, status=status.HTTP_200_OK)


class ExpertiseDetails(APIView):
    """
    This endpoint returns my technical expertise details
    """
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        """
        Return of a list of technical expertise
        :param request:
        :param format:
        :return: JSON object array containing expertise details
        """
        expertise = Expertise.objects.all()
        expertise_serializer = ExpertiseSerializer(expertise, many=True)
        return Response(expertise_serializer.data, status=status.HTTP_200_OK)


class ProgrammingDetails(APIView):
    """
    This endpoint returns the programming languages and frameworks I am familiar with
    """
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        programming_framework_skills = TechnicalSkill.objects.filter(
            skill_type__in=[TechnicalSkill.PROGRAMMING_LANGUAGE, TechnicalSkill.FRAMEWORK]
        )
        skills_serializer = TechnicalSkillSerializer(programming_framework_skills, many=True)
        return Response(skills_serializer.data, status=status.HTTP_200_OK)


class DevelopmentToolDetails(APIView):
    """
    This endpoint returns the development tools I am familiar with
    """
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        development_tool_skills = TechnicalSkill.objects.filter(
            skill_type=TechnicalSkill.DEV_TOOL
        )
        skills_serializer = TechnicalSkillSerializer(development_tool_skills, many=True)
        return Response(skills_serializer.data, status=status.HTTP_200_OK)


class DataStorageDetails(APIView):
    """
    This endpoint returns the data storage technologies I am familiar with
    """
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        data_skills = TechnicalSkill.objects.filter(
            skill_type=TechnicalSkill.DATA
        )
        skills_serializer = TechnicalSkillSerializer(data_skills, many=True)
        return Response(skills_serializer.data, status=status.HTTP_200_OK)


class DeploymentDetails(APIView):
    """
    This endpoint returns the deployment tools I am familiar with
    """
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        deployment_skills = TechnicalSkill.objects.filter(
            skill_type=TechnicalSkill.DEPLOYMENT
        )
        skills_serializer = TechnicalSkillSerializer(deployment_skills, many=True)
        return Response(skills_serializer.data, status=status.HTTP_200_OK)
