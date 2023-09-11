from django.db import models
from .base import BaseModel


class Transaction(BaseModel):
    TYPE = (
        ("Buy", "Buy"),
        ("Sell", "Sell"),
    )
    user_id = models.ForeignKey("User", related_name="user_id", on_delete=models.CASCADE)
    ticker = models.CharField(max_length=30)
    transaction_type = models.CharField(max_length=10, choices=TYPE, default="Buy")
    transaction_volume = models.IntegerField()
    transaction_price = models.FloatField()

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
