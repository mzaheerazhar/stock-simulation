from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from market_simulation.models import User
from market_simulation.serializers.user_serializer import UserSerializer


class GetUserByUsernameAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            data = {
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
            }
            return Response(data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class GetAllUserAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            users_data = User.objects.all()
            serializer = UserSerializer(users_data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'detail': 'Users not found'}, status=status.HTTP_404_NOT_FOUND)

