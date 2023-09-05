from rest_framework import serializers
from market_simulation.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializers registration requests and creates a new user.
    """
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "password", "balance"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
