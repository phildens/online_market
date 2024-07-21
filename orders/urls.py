from django.urls import path
from .views import all_orders, order_details, add_order

urlpatterns = [
    path('', all_orders, name='all_orders'),
    path('<int:order_id>/', order_details, name='order_details'),
    path('create/', add_order, name='add_order'),

]
