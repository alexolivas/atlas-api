from rest_framework import serializers

from atlas.web.models import AboutInfo


class AboutInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutInfo
        fields = (
            'location',
            'description'
        )
