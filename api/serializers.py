from rest_framework import serializers
from .models import Customer, Products, Cart, Types, Orders


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields ='__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

# class OrderProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderProduct
#         fields = '__all__'

# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cart
#         fields = ('cart_id', 'items')


# class TypesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Types
#         fields = ('type_id', 'type_name')


# class CarTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CarType
#         fields = ('typeId', 'description', 'dailyCost', 'weeklyCost',
#                   'monthlyCost', 'lateFee', 'changeBranchFee')


