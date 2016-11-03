from rest_framework import serializers
from web.models import Technology


class TechnologySerializer(serializers.ModelSerializer):

    class Meta:
        model = Technology
        fields = (
            'id',
            'name'
        )
