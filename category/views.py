from itertools import product

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

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


class ProductInCategoryListView(APIView):
    def get(self, request, category_id):
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        subcategories = SubCategory.objects.filter(category=category)
        products = Product.objects.filter(sub_category__in=subcategories)
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubCategoryProductListView(APIView):
    def get(self, request, category_id):
        try:
            sub_category = SubCategory.objects.get(pk=category_id)
        except SubCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        products = Product.objects.filter(sub_category=sub_category)
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
