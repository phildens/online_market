from rest_framework import serializers

from products.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'representation', 'price', 'image_url')


class ProductFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
