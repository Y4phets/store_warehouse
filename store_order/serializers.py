from rest_framework import serializers

from .models import StoreOrder


class StoreOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoreOrder
        fields = ("order_number", "status", "warehouse_order_id", "warehouse_account")
