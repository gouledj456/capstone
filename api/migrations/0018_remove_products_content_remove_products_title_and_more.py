# Generated by Django 4.1.3 on 2023-02-20 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_products_content_products_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='content',
        ),
        migrations.RemoveField(
            model_name='products',
            name='title',
        ),
        migrations.AddField(
            model_name='products',
            name='product_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='products',
            name='product_description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='products',
            name='product_height',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='product_name',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='product_price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='product_price_sale',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='product_quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='product_weight',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='type_foreign_key',
            field=models.ManyToManyField(blank=True, related_name='Types', to='api.types'),
        ),
    ]
