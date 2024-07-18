from django.contrib import admin
from .models import *


@admin.register(Product, Category, SubCategory)
class ProductAdmin(admin.ModelAdmin):
    pass
