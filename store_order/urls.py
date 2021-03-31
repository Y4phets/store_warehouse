from django.urls import path, include
from rest_framework import routers
from .views import StoreOrderView

app_name = "store_order"

router = routers.DefaultRouter()
router.register(r"store_order", StoreOrderView, basename="store_order")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

