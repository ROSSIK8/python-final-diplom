# Generated by Django 4.2.4 on 2023-09-22 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_rename_orders_basket_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='order',
            field=models.ManyToManyField(blank=True, null=True, related_name='basket', to='main.order', verbose_name='Заказ'),
        ),
    ]
