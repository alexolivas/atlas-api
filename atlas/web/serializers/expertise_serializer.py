from rest_framework import serializers

from atlas.web.models import Expertise


class ExpertiseSerializer(serializers.ModelSerializer):
    area = serializers.SerializerMethodField()

    class Meta:
        model = Expertise
        fields = (
            'area',
            'font_awesome_icon',
            'description'
        )

    def get_area(self,obj):
        return obj.get_area_display()
