# Generated by Django 4.1.3 on 2023-01-31 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_cart_item_orders_orders_products_types_delete_branch_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='card_number',
            field=models.IntegerField(blank=True, max_length=17),
        ),
    ]
