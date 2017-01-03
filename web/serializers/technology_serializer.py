from rest_framework import serializers
from web.models import TechnicalSkill


class TechnicalSkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = TechnicalSkill
        fields = (
            'id',
            'name'
        )
