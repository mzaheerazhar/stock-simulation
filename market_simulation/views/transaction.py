from datetime import datetime

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from market_simulation.common.custom_exceptions import NoContentException
from market_simulation.models import Transaction, StockData
from market_simulation.serializers import TransactionSerializer
from stock_market_simulation.celery import app as celery_app


class TransactionAPIView(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        trans = request.data
        users_data = {
            "id": request.user.id,
            "balance": request.user.balance
        }
        make_transaction.delay(trans, users_data, *args, **kwargs)
        return Response(
            {
                "success": True,
                "message": "Transaction send successfully"
            },
            status=status.HTTP_200_OK,
        )


def calculate_price(stock_data, trans):
    if trans.get('transaction_type') == '0':
        return stock_data.low * int(trans.get('transaction_volume'))
    return stock_data.high * int(trans.get('transaction_volume'))


@celery_app.task()
def make_transaction(trans, user, *args, **kwargs):

    if trans.get("user_id") != str(user.get("id")):
        raise NoContentException()
    stock_data = StockData.objects.filter(ticker=trans.get("ticker")).first()
    if not stock_data:
        raise NoContentException()
    transaction_price = calculate_price(stock_data, trans)

    if trans.get('transaction_type') == "0":
        new_balance = user.get("balance") - transaction_price
    else:
        new_balance = user.get("balance") + transaction_price
    if new_balance < 0:
        return Response({
            "success": False,
            "message": "Insufficient Balance"
        },
            status=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    stock_data.volume = stock_data.volume - int(trans.get('transaction_volume'))
    stock_data.save()

    trans_data = dict(trans)  # Create a new dictionary from trans
    trans_data['transaction_type'] = int(trans.get('transaction_type'))
    trans_data['ticker'] = stock_data.ticker
    trans_data['transaction_price'] = transaction_price
    trans_data['user_id'] = user.get("id")
    trans_data['transaction_volume'] = int(trans.get('transaction_volume'))
    serializer = TransactionSerializer(data=trans_data)
    serializer.is_valid(raise_exception=True)
    serializer.save()


class TransactionByUserAPIView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TransactionSerializer

    def list(self, request, user_id):
        try:
            trans_data = Transaction.objects.filter(user_id=user_id).all()
            serializer = self.serializer_class(instance=trans_data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Transaction.DoesNotExist:
            return Response({'detail': 'Transaction not found against this user'}, status=status.HTTP_404_NOT_FOUND)


class TransactionByUserAndDateAPIView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TransactionSerializer

    def list(self, request, user_id, start, end):
        try:
            start_date = datetime.strptime(start, '%Y-%m-%d')
            end_date = datetime.strptime(end, '%Y-%m-%d')

            trans_data = Transaction.objects.filter(user_id=user_id, created_at__range=(start_date, end_date))
            serializer = self.serializer_class(trans_data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
            return Response({'detail': 'Invalid date format'}, status=status.HTTP_400_BAD_REQUEST)
