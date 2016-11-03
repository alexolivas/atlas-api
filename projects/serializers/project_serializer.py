from rest_framework import serializers
from accounts.serializers.account_overview_serializer import AccountOverviewSerializer
from projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    account = AccountOverviewSerializer()

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
