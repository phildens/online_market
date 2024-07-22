from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Order, OrderItem
from .serializers import OrderSerializer, DetailOrderSerializer
from products.models import Product


# Create your views here.
@api_view(['GET'])
@authentication_classes((TokenAuthentication, BasicAuthentication, SessionAuthentication))
@permission_classes([IsAuthenticated])
def all_orders(request):
    if request.method == 'GET':
        user = request.user
        try:
            order_list = Order.objects.filter(user=user)
        except Order.DoesNotExist:
            return Response({'error': 'Orders not found'},status=status.HTTP_404_NOT_FOUND)
        order_serializer = OrderSerializer(order_list, many=True)
        return Response({'Orders': order_serializer.data})


@api_view(['GET'])
@authentication_classes((TokenAuthentication, BasicAuthentication, SessionAuthentication))
@permission_classes([IsAuthenticated])
def order_details(request, order_id):
    if request.method == 'GET':
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({'Order': 'Order not found'},status=status.HTTP_404_NOT_FOUND)

        order_serializer = DetailOrderSerializer(order)
        return Response({'Order': order_serializer.data})


@api_view(['POST'])
@authentication_classes((TokenAuthentication, BasicAuthentication, SessionAuthentication))
@permission_classes([IsAuthenticated])
def add_order(request):
    if request.method == 'POST':
        user = request.user
        order = Order.objects.create(user=user)
        for i in request.data['items']:
            OrderItem.objects.create(order=order, product=Product.objects.get(id=i['product_id']), total=i['total'])

        order_serializer = DetailOrderSerializer(order)
        return Response({'Order': order_serializer.data})

