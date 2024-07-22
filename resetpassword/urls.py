from django.urls import path
from resetpassword.views import reset_password_auth, reset_fargot_password, confirm_code, reset_password
urlpatterns = [
    path('', reset_password_auth, name='reset_password'),
    path('forgot/', reset_fargot_password, name='reset_password'),
    path('confirm_code/', confirm_code, name='confirm_code'),
    path('reset_password/', reset_password, name='reset_password_token'),
]