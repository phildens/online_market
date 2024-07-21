from django.contrib import admin
from .models import Product, Category, SubCategory


@admin.register(Product, Category, SubCategory)
class ProductAdmin(admin.ModelAdmin):
    pass
