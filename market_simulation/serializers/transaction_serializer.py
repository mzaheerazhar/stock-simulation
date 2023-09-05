from rest_framework import serializers
from market_simulation.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    """
    Serializers creates transaction and update.
    """
    class Meta:
        model = Transaction
        fields = "__all__"

    # def create(self, validated_data):
    #     return Transaction.objects.create(**validated_data)
