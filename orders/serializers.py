from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from orders.models import Order, OrderItem, PaymentDetails


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        order = Order(
            user=validated_data['user'],
        )

        return order


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class DetailOrderSerializer(serializers.ModelSerializer):
    items = SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'date_ordered', 'items']

    def get_items(self, obj):
        items = OrderItem.objects.filter(order=obj)
        items_serializer = OrderItemSerializer(items, many=True)
        return items_serializer.data


class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = '__all__'
