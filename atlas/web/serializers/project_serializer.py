from rest_framework import serializers

from atlas.projects.models import Project, ProjectPhoto
from atlas.web.serializers.technology_serializer import TechnicalSkillSerializer


class ProjectPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPhoto
        fields = ('photo', 'main_photo', 'project',)


class ProjectSerializer(serializers.ModelSerializer):
    technology = TechnicalSkillSerializer(read_only=True, many=True)
    photos = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'production_url',
            'repo_url',
            'technology',
            'tech_stack_display',
            'description',
            'technology_description',
            'public_repo',
            'photos',
        )

    def get_photos(self, object):
        return ProjectPhoto.objects.filter(project=object.id)
