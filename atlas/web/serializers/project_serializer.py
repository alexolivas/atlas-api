from rest_framework import serializers

from atlas.projects.models import Project, ProjectPhoto
from atlas.web.serializers.technology_serializer import TechnicalSkillSerializer


class ProjectPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPhoto
        fields = ('url', 'main_photo', 'project',)


class ProjectSerializer(serializers.ModelSerializer):
    technology = TechnicalSkillSerializer(read_only=True, many=True)
    photos = serializers.SerializerMethodField()
    main_photo = serializers.SerializerMethodField()

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
            'main_photo',
            'photos',
        )

    def get_photos(self, instance):
        project_photos = ProjectPhoto.objects.filter(project=instance.id)
        serializer = ProjectPhotoSerializer(project_photos, many=True)
        return serializer.data

    def get_main_photo(self, instance):
        main_photos = ProjectPhoto.objects.filter(project=instance.id, main_photo=True)
        if main_photos:
            serializer = ProjectPhotoSerializer(main_photos[0])
            return serializer.data
        return ''
