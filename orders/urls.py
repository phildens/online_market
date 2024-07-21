from django.urls import path
from .views import all_orders

urlpatterns = [
    path('', all_orders, name='checkout'),

]
