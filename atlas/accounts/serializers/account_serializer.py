from rest_framework import serializers

from atlas.accounts import Account


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'
