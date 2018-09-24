from rest_framework import serializers

from atlas.projects.models import Project
from atlas.web.serializers.technology_serializer import TechnicalSkillSerializer


# TODO: Delete this and only keep PortfolioSerializer
class PortfolioDetailSerializer(serializers.ModelSerializer):
    technology = TechnicalSkillSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'active_development',
            'main_photo',
            'description',
            'technology_description',
            'production_url',
            'technology'
        )
