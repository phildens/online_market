from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from orders.models import Order, OrderItem, PaymentDetails


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    price = SerializerMethodField()
    item_name = SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'total', 'price', 'item_name']


    def get_price(self, obj):
        return obj.product.price

    def get_item_name(self, obj):
        return obj.product.name


class DetailOrderSerializer(serializers.ModelSerializer):
    items = SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'date_ordered', 'items']

    def get_items(self, obj):
        items = OrderItem.objects.filter(order=obj)
        items_serializer = OrderItemSerializer(items, many=True)
        return items_serializer.data
    # def get_payment_details(self, obj):
    #     payment_details = PaymentDetails.objects.filter(order=obj)
    #     payment_details_serializer = PaymentDetailsSerializer(payment_details)
    #     return payment_details_serializer.data


class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = '__all__'
