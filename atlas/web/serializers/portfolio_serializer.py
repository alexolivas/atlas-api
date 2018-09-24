from rest_framework import serializers

from atlas.projects import Project
from atlas.web.serializers.technology_serializer import TechnicalSkillSerializer


class PortfolioSerializer(serializers.ModelSerializer):
    technology = TechnicalSkillSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'main_photo',
            'main_photo_thumb',
            'production_url',
            'repo_url',
            'technology',
            'tech_stack_display',
            'description',
            'technology_description',
            'public_access',
            'photo_1',
            'photo_2',
            'photo_3',
            'photo_4',
            'photo_5',
            'photo_6',
            'photo_7',
            'photo_8',
            'photo_9'
        )
