from django.shortcuts import render
from rest_framework.generics import ListAPIView

from category.models import Category, SubCategory
from category.serializers import CategorySerializer, SubCategorySerializer


# Create your views here.
class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryListView(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
