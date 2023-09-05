from rest_framework import serializers
from market_simulation.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializers registration requests and creates a new user.
    """
    class Meta:
        model = User
        fields = "__all__"

