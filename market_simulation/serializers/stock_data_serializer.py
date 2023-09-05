from rest_framework import serializers
from market_simulation.models import StockData


class StockSerializer(serializers.ModelSerializer):
    """
    Serializers creates stock and update.
    """
    class Meta:
        model = StockData
        fields = "__all__"

    def create(self, validated_data):
        return StockData.objects.create(**validated_data)
