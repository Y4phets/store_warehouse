import requests
from django.contrib import admin

from .models import StoreOrder, WarehouseAccount


@admin.register(WarehouseAccount)
class WarehouseAccountAdmin(admin.ModelAdmin):
    list_display = ['pk', 'warehouse_name', 'end_point']
    search_fields = ('warehouse_name',)


@admin.register(StoreOrder)
class StoreOrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'order_number', 'status']
    search_fields = ('order_number', 'status',)

    def save_model(self, request, obj, form, change):
        s = obj.id
        url = obj.warehouse_account.end_point
        data = {
            "store_order_id": obj.pk if obj.pk else None,
            "order_number": obj.order_number,
            "status": obj.status,
            "end_point": f"http://0.0.0.0:8000/api/v1/store_order/"
        }
        response = requests.patch(f"http://0.0.0.0:8001/api/v1/warehouse_order/{s}/",
                                  data=data) if obj.pk else requests.post(url, data=data)
        obj.save()
