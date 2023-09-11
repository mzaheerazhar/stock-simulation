from datetime import datetime

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from market_simulation.celery_services.tasks import make_transaction
from rest_framework.views import APIView
from market_simulation.common.custom_exceptions import NoContentException

from market_simulation.models import Transaction
from market_simulation.serializers import TransactionSerializer
import market_simulation.common.constants as constant


class TransactionAPIView(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        users_data = {
            "id": request.user.id,
            "balance": request.user.balance
        }
        
        if request.data.get("user_id") != str(request.user.id):
            raise NoContentException()
        
        make_transaction.delay(request.data, users_data, *args, **kwargs)
        return Response(
            {
                "success": True,
                "message": constant.TRANSACTION_QUEUED
            },
            status=status.HTTP_200_OK,
        )


class TransactionByUserAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TransactionSerializer

    def get(self, request, user_id):
        transaction_data = Transaction.objects.all()
        print(transaction_data)
        serializer = self.serializer_class(transaction_data, many=True)
        if not transaction_data:
            return Response({'detail': constant.TRANSACTION_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TransactionByUserAndDateAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TransactionSerializer

    def get(self, request, user_id, start, end):
        try:
            start_date = datetime.strptime(start, '%Y-%m-%d')
            end_date = datetime.strptime(end, '%Y-%m-%d')
        except ValueError:
            return Response({'detail': constant.INVALID_DATE}, status=status.HTTP_400_BAD_REQUEST)
        
        transaction_data = Transaction.objects.filter(
            user_id=user_id, created_at__range=(start_date, end_date))
        serializer = self.serializer_class(transaction_data, many=True)
        if not transaction_data:
            return Response({'detail': constant.TRANSACTION_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)
