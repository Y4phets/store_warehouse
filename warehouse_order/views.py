from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import WarehouseOrder
from .serializers import WarehouseOrderSerializer


class WarehouseOrderView(viewsets.ModelViewSet):
    queryset = WarehouseOrder.objects.all()
    filter_fields = ("order_number", "status",)
    serializer_class = WarehouseOrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
