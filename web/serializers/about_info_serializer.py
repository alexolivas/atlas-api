from rest_framework import serializers
from web.models import AboutInfo


class AboutInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutInfo
        fields = '__all__'
