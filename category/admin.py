from django.contrib import admin
from category.models import Category, SubCategory


# Register your models here.
@admin.register(Category, SubCategory)
class ProductAdmin(admin.ModelAdmin):
    pass
