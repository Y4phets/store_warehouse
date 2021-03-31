from rest_framework import viewsets

from .models import StoreOrder
from .serializers import StoreOrderSerializer


class StoreOrderView(viewsets.ModelViewSet):

    queryset = StoreOrder.objects.all()
    filter_fields = ("order_number", "status",)
    serializer_class = StoreOrderSerializer
