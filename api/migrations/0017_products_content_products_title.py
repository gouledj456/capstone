# Generated by Django 4.1.3 on 2023-02-20 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_remove_products_product_available_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='products',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
