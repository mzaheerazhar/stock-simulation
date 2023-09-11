from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from market_simulation.models import User
from market_simulation.serializers.user_serializer import UserSerializer
import market_simulation.common.constants as constant


class GetUserByUsernameAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, username):
        user_data = User.objects.get(username=username)
        serializer = UserSerializer(user_data)
        if not user_data:
            return Response({"detail": constant.USER_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetAllUserAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users_data = User.objects.all()
        serializer = UserSerializer(users_data, many=True)
        if not users_data:
            return Response({"detail": constant.USER_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)            
