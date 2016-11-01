from rest_framework import serializers
from projects.models import Project


class ProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', 'main_photo', 'production_url', 'technology',)
