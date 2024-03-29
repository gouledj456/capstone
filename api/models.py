from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Types(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50)

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=80)
    product_description = models.CharField(max_length=200)
    product_quantity = models.PositiveIntegerField()
    product_price = models.FloatField()
    product_price_sale = models.FloatField(blank=True)
    product_available = models.BooleanField()
    product_weight = models.FloatField()
    product_height = models.FloatField()
    image = models.ImageField(upload_to='frontend/src/productimages', blank=True)
    type_foreign_key = models.ManyToManyField(Types, related_name="Types", blank=True)
    
    def __str__(self):
        return self.product_name


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    items = models.OneToOneField('Products', related_name='Carts', default='', on_delete=models.CASCADE)

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    # customerPhone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    address_line = models.CharField(max_length=120, default="")
    postal_code = models.CharField(max_length=8)
    city = models.CharField(max_length=60)
    province = models.CharField(max_length=60)
    country = models.CharField(max_length=60)

    
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_time = models.DateTimeField(auto_now_add=True, blank=True)
    order_total = models.FloatField(default=0.00, validators=[MinValueValidator(0.00)])
    customer = models.ForeignKey('Customer', related_name='Orders', default='', on_delete=models.CASCADE)
    products = models.CharField(blank=True, max_length=255)

    order_status = models.BooleanField(default=False)
