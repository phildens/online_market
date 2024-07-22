from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from resetpassword.email_sent import send_reset_mail
from user_buyer.models import CustomUser
from resetpassword.models import ResetPassword


# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reset_password_auth(request):
    user = request.user
    user.set_password(request.data['password'])
    user.save()
    return Response('Password reset')


@api_view(['POST'])
def reset_fargot_password(request):
    username = request.data['username']

    user = None
    if '@' in username:
        try:
            user = CustomUser.objects.get(email=username)
        except CustomUser.DoesNotExist:
            return Response('invalid username', status=status.HTTP_400_BAD_REQUEST)
    if user is None:
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return Response('invalid username', status=status.HTTP_400_BAD_REQUEST)

    if user:
        if ResetPassword.objects.filter(user=user).exists():
            ResetPassword.objects.filter(user=user).delete()
        code = send_reset_mail(user.email)
        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)
        reset = ResetPassword(user=user, reset_code=code, token=token)
        reset.save()
        return Response('check email', status=status.HTTP_200_OK)
    else:
        return Response('invalid username', status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def confirm_code(request):
    code = request.data['code']
    username = request.data['username']
    print(code, username, 'fdfdfd')
    try:
        if '@' in username:
            user = CustomUser.objects.get(email=username)
        else:
            user = CustomUser.objects.get(username=username)
        reset_pass = ResetPassword.objects.get(user=user)
    except ResetPassword.DoesNotExist or CustomUser.DoesNotExist:
        return Response('invalid code', status=status.HTTP_400_BAD_REQUEST)
    if reset_pass.reset_code != code:
        return Response('invalid code', status=status.HTTP_400_BAD_REQUEST)
    return Response({'Token': reset_pass.token})


@api_view(['POST'])
def reset_password(request):
    token = request.data['Token']
    password = request.data['password']
    try:
        reset_pass = ResetPassword.objects.get(token=token)
    except:
        return Response('invalid token', status=status.HTTP_400_BAD_REQUEST)

    user = reset_pass.user
    user.set_password(password)
    user.save()
    reset_pass.delete()
    return Response({'username': user.username, 'password': password})
