from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Order, OrderItem, PaymentDetails
from rest_framework import generics
from .serializers import OrderSerializer, OrderItemSerializer, DetailOrderSerializer


# Create your views here.
@api_view(['GET'])
@authentication_classes((TokenAuthentication, BasicAuthentication, SessionAuthentication))
@permission_classes([IsAuthenticated])
def all_orders(request):
    if request.method == 'GET':
        user = request.user
        order_list = Order.objects.filter(user=user)
        order_serializer = OrderSerializer(order_list, many=True)
        return Response({'Orders': order_serializer.data})


@api_view(['GET'])
@authentication_classes((TokenAuthentication, BasicAuthentication, SessionAuthentication))
@permission_classes([IsAuthenticated])
def order_details(request, order_id):
    order = Order.objects.get(id=order_id)

    order_serializer = DetailOrderSerializer(order)
    return Response({'Order': order_serializer.data })
