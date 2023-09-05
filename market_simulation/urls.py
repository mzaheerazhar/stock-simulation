from django.urls import path
from market_simulation.views import (
    RegistrationAPIView,
    StockDataAPIView,
    TransactionAPIView,
    TransactionByUserAPIView,
    TransactionByUserAndDateAPIView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from market_simulation.views.user import GetUserByUsernameAPIView, GetAllUserAPIView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/<str:username>/', GetUserByUsernameAPIView.as_view(), name='get_user_by_username'),
    path('users/', GetAllUserAPIView.as_view(), name='get_all_users'),
    path("register/", RegistrationAPIView.as_view(), name="registration"),
    path("stock/", StockDataAPIView.as_view({'get': 'list', 'post': 'create', 'patch': 'update'}), name="stock_data"),
    path("transaction/", TransactionAPIView.as_view({'post': 'create'}), name="transaction"),
    path("transaction/<str:user_id>/", TransactionByUserAPIView.as_view({'get': 'list'}), name="transaction"),
    path("transactions/<str:user_id>/<str:start>/<str:end>/", TransactionByUserAndDateAPIView.as_view({'get': 'list'}), name="transactions"),
]
