from rest_framework import serializers

from .models import WarehouseOrder


class WarehouseOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = WarehouseOrder
        fields = ("order_number", "status", "store_order_id", "store_account",)
