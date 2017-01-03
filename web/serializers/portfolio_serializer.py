from rest_framework import serializers
from projects.models import Project
from web.serializers.technology_serializer import TechnicalSkillSerializer


class PortfolioSerializer(serializers.ModelSerializer):
    technology = TechnicalSkillSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'main_photo',
            'production_url',
            'technology'
        )
