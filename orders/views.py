from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
@authentication_classes((TokenAuthentication, SessionAuthentication))
@permission_classes([IsAuthenticated])
def checkout(request):
    if request.method == 'GET':
        user = request.user

        return Response({'message': 'ok'})