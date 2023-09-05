from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models.user import User
from .models.stock_data import StockData
from .models.transactions import Transaction

admin.site.register(User, UserAdmin)
admin.site.register(StockData)
admin.site.register(Transaction)
