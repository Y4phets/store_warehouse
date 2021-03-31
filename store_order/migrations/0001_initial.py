# Generated by Django 3.1.5 on 2021-01-24 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WarehouseAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse_name', models.CharField(max_length=255)),
                ('end_point', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StoreOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('NEW', 'New'), ('IN_PROCESS', 'In Process'), ('STORED', 'Stored'), ('SEND', 'Send')], max_length=25)),
                ('warehouse_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_order.warehouseaccount')),
            ],
        ),
    ]
