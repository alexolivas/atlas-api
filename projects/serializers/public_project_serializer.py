from rest_framework import serializers
from projects.models import Project


class PublicProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        # fields = '__all__'
        fields = ('id', 'name', 'main_photo', 'production_url', 'technology',)
