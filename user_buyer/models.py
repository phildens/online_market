from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)

    def __str__(self):
        return self.phone + ' '+ self.first_name + ' ' + self.last_name