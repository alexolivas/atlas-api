from rest_framework import serializers
from web.models import TechnicalSkill


class TechnicalSkillSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = TechnicalSkill
        fields = (
            'name',
            'type',
            'description'
        )

    @staticmethod
    def get_type(obj):
        return obj.get_skill_type_display()
