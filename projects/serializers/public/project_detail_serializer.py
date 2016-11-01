from rest_framework import serializers
from projects.models import Project


class ProjectDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', 'active_development', 'main_photo', 'description', 'technology_description',
                  'production_url', 'technology',)
