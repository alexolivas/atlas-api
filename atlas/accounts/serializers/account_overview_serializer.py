from rest_framework import serializers

from atlas.accounts import Account


class AccountOverviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = (
            'id',
            'name',
            'account_number',
            'industry'
        )
