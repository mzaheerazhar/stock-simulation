from market_simulation.common.helper_methods import calculate_price
from market_simulation.common.custom_exceptions import NoContentException
from market_simulation.models import StockData
from stock_market_simulation.celery import app as celery_app
from rest_framework.response import Response
from rest_framework import status
from market_simulation.serializers import TransactionSerializer
import market_simulation.common.constants as constant


@celery_app.task()
def make_transaction(transaction, user, *args, **kwargs):
    stock_data = StockData.objects.filter(ticker=transaction.get("ticker")).first()
    if not stock_data:
        raise NoContentException()
    transaction_price = calculate_price(stock_data, transaction)

    if transaction.get('transaction_type') == "Buy":
        new_balance = user.get("balance") - transaction_price
    else:
        new_balance = user.get("balance") + transaction_price
    if new_balance < 0:
        return Response({
            "success": False,
            "message": constant.INSUFFICIENT_BALANCE
        },
            status=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
    stock_data.volume = stock_data.volume - \
        int(transaction.get('transaction_volume'))
    stock_data.save()

    transaction['transaction_price'] = transaction_price
    serializer = TransactionSerializer(data=transaction)
    serializer.is_valid(raise_exception=True)
    serializer.save()
