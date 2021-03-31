import requests
from django.contrib import admin

from .models import WarehouseOrder, StoreAccount


@admin.register(StoreAccount)
class StoreAccountAdmin(admin.ModelAdmin):
    list_display = ['pk', 'store_name', 'end_point']
    search_fields = ('store_name',)


@admin.register(WarehouseOrder)
class WarehouseOrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'order_number', 'status']
    search_fields = ('order_number', 'status',)

    def save_model(self, request, obj, form, change):
        s = ""
        # если пустые кварги, то обновление. если не пустые, то создание
        # http://0.0.0.0:8001/api/v1/store_order/3/
        s = obj.id
        url = obj.warehouse_account.end_point
        data = {
            "order_number": obj.order_number,
            "status": obj.status,
            "end_point": f"http://0.0.0.0:8001/api/v1/warehouse_order/"
        }
        response = requests.patch(f"http://0.0.0.0:8001/api/v1/store_order/{s}/",
                                  data=data) if obj.pk else requests.post(url, data=data)
        obj.save()
