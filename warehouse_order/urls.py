from django.urls import path, include
from rest_framework import routers
from .views import WarehouseOrderView

app_name = "warehouse_order"

router = routers.DefaultRouter()
router.register(r"warehouse_order", WarehouseOrderView, basename="warehouse_order")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

