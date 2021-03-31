from django.db import models

STATUS = (
    ('NEW', 'New'),
    ('IN_PROCESS', 'In Process'),
    ('STORED', 'Stored'),
    ('SEND', 'Send'),
)


class StoreAccount(models.Model):
    store_name = models.CharField(max_length=255, unique=True)
    end_point = models.CharField(max_length=255)

    def __str__(self):
        return self.store_name


class WarehouseOrder(models.Model):
    order_number = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=25, choices=STATUS)
    store_order_id = models.PositiveIntegerField(blank=True, null=True)

    store_account = models.ForeignKey(StoreAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_number
