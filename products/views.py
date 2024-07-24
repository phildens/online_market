from rest_framework import generics
from products.models import Product
from products.serializers import ProductListSerializer, ProductFullSerializer
from rest_framework import filters


# Create your views here.
class ProductListAll(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'full_description', 'representation')


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFullSerializer
