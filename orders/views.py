from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Order, OrderItem, PaymentDetails
from rest_framework import generics
from .serializers import OrderSerializer

# Create your views here.
@api_view(['GET'])
@authentication_classes((TokenAuthentication, SessionAuthentication))
@permission_classes([IsAuthenticated])
def checkout(request):
    if request.method == 'GET':
        user = request.user
        order_list = Order.objects.filter(user=user)
        order_serializer = OrderSerializer(order_list, many=True)
        return Response(order_serializer.data)