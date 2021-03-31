from django.db import models

STATUS = (
    ('NEW', 'New'),
    ('IN_PROCESS', 'In Process'),
    ('STORED', 'Stored'),
    ('SEND', 'Send'),
)


class WarehouseAccount(models.Model):
    warehouse_name = models.CharField(max_length=255, unique=True)
    end_point = models.CharField(max_length=255)

    def __str__(self):
        return self.warehouse_name


class StoreOrder(models.Model):
    order_number = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=25, choices=STATUS)
    warehouse_order_id = models.PositiveIntegerField(blank=True, null=True)

    warehouse_account = models.ForeignKey(WarehouseAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_number
