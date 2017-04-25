from rest_framework import serializers
from web.models import AboutInfo


class AboutInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutInfo
        fields = (
            'home_page_description',
            'about_page_description',
            'personal_description'
        )
