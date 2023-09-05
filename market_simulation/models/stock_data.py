from django.db import models
from .base import BaseModel


class StockData(BaseModel):
    ticker = models.CharField(max_length=30)
    open_price = models.IntegerField()
    close_price = models.IntegerField()
    high = models.IntegerField()
    low = models.IntegerField()
    volume = models.IntegerField()

    class Meta:
        verbose_name = "StockData"
        verbose_name_plural = "StocksData"
