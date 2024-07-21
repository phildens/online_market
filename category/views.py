from itertools import product

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from products.serializers import ProductListSerializer
from category.models import Category, SubCategory
from category.serializers import CategorySerializer, SubCategorySerializer
from products.models import Product


# Create your views here.
class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryListView(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

@api_view(['GET'])
def product_in_subcategory(request, category_id):
    sub_category = SubCategory.objects.get(pk=category_id)
    products = Product.objects.filter(sub_category=sub_category)
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)