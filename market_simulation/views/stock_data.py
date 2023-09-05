from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from market_simulation.models import StockData
from market_simulation.serializers import StockSerializer


class StockDataAPIView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    ordering = ("created_at",)
    serializer_class = StockSerializer

    def get_queryset(self):
        queryset = StockData.objects.all()
        stock_id = self.request.GET.get('id')
        if stock_id:
            queryset = [StockData.objects.filter(id=stock_id).first()]
        return queryset

    def create(self, request, *args, **kwargs):
        stock = request.data
        stock["user"] = request.user.id
        serializer = self.serializer_class(data=stock)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "success": True,
                "message": "stock has been created"
            },
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, *args, **kwargs):
        stock = request.data
        instance = StockData.objects.filter(id=stock.get("id")).first()
        serializer = self.serializer_class(instance, data=stock, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "success": True,
                "message": "stock has been updated"
            },
            status=status.HTTP_200_OK,
        )
