# Generated by Django 4.2.4 on 2023-10-18 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_rename_products_basket_orders_delete_mainorders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='state',
        ),
    ]
