from django.db import models
from user_buyer.models import CustomUser


# Create your models here.
class ResetPassword(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=100)
    reset_date = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=100)

    def __str__(self):
        return f'user: {self.user.id} date: {self.reset_date} code: {self.reset_code}'
