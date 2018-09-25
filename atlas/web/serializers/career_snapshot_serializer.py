from rest_framework import serializers

from atlas.web.models import CareerSnapshot


class CareerSnapshotSerializer(serializers.ModelSerializer):

    class Meta:
        model = CareerSnapshot
        fields = (
            'id',
            'company',
            'position',
            'location',
            'snapshot_type',
            'month',
            'year',
            'description'
        )
