from rest_framework import generics
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductListSerializer, ProductFullSerializer


# Create your views here.
class ProductListAll(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFullSerializer
