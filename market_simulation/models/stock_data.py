from django.db import models
from .base import BaseModel


class StockData(BaseModel):
    ticker = models.CharField(max_length=30)
    open_price = models.FloatField()
    close_price = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    volume = models.IntegerField()

    class Meta:
        verbose_name = "StockData"
        verbose_name_plural = "StocksData"
