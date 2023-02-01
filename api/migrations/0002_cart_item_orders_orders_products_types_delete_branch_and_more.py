# Generated by Django 4.1.3 on 2023-01-31 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Item_Orders',
            fields=[
                ('item_order_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_order_quantity', models.IntegerField()),
                ('item_order_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_time', models.DateField()),
                ('orde_total', models.IntegerField()),
                ('item_order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.item_orders')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=80)),
                ('product_description', models.CharField(max_length=200)),
                ('product_quantity', models.IntegerField()),
                ('product_price', models.FloatField()),
                ('product_price_sale', models.FloatField()),
                ('product_available', models.BooleanField()),
                ('product_height', models.FloatField()),
                ('product_weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='CarType',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Rental',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='dob',
            new_name='card_expire_date',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customerID',
            new_name='customer_id',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='unitNumber',
            new_name='unit',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='driversLicense',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='goldMember',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='postalCode',
        ),
        migrations.AddField(
            model_name='customer',
            name='card_address',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='card_name',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='card_number',
            field=models.IntegerField(default=1, max_length=17),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='country',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='cvc_number',
            field=models.IntegerField(default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='postal_code',
            field=models.CharField(default='', max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='province',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='customer',
            name='streetName',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='streetNumber',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='products',
            name='type_foreign_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.types'),
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(related_name='carts', to='api.products'),
        ),
        migrations.AddField(
            model_name='customer',
            name='Order_foreign_key',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.orders', blank='true', null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='cart',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.cart', blank='true', null=True),
            preserve_default=False,
        ),
    ]