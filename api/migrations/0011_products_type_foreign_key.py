# Generated by Django 4.1.3 on 2023-01-31 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_customer_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='type_foreign_key',
            field=models.ManyToManyField(related_name='Types', to='api.types'),
        ),
    ]
