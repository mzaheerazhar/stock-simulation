from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from market_simulation.serializers.registration_serializer import RegistrationSerializer
import market_simulation.common.constants as constant


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "success": True,
                "message": constant.REGISTERATION_SUCCESS
            },
            status=status.HTTP_201_CREATED,
        )
