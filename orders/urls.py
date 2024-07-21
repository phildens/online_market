from django.urls import path
from .views import all_orders, order_details

urlpatterns = [
    path('', all_orders, name='checkout'),
    path('<int:order_id>/', order_details, name='checkout'),

]
