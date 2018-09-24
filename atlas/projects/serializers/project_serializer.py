from rest_framework import serializers

from atlas.accounts import AccountOverviewSerializer
from atlas.projects import Project
from atlas.web.serializers.technology_serializer import TechnicalSkillSerializer


class ProjectSerializer(serializers.ModelSerializer):
    account = AccountOverviewSerializer()
    technology = TechnicalSkillSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = (
            'name',
            'account',
            'active_development',
            'project_completed',
            'display_on_website',
            'retired',
            'main_photo',
            'description',
            'technology_description',
            'repo_url',
            'stage_url',
            'production_url',
            'technology'
        )
