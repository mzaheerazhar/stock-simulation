from django.db import models
from .base import BaseModel


class Transaction(BaseModel):
    TYPE = (
        (0, "Buy"),
        (1, "Sell"),
    )
    user_id = models.ForeignKey("User", related_name="user_id", on_delete=models.CASCADE)
    ticker = models.CharField(max_length=30)
    transaction_type = models.IntegerField(choices=TYPE, default=0)
    transaction_volume = models.IntegerField()
    transaction_price = models.IntegerField()

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
