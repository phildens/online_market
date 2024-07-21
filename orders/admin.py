from django.contrib import admin
from .models import Order, OrderItem, PaymentDetails


@admin.register(Order, OrderItem, PaymentDetails)
class OrderAdmin(admin.ModelAdmin):
    pass
