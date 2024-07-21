from django.db import models
from category.models import Category, SubCategory

class Product(models.Model):
    name = models.CharField(max_length=100)
    representation = models.CharField(max_length=1000)
    price = models.IntegerField()
    country = models.CharField(max_length=100)
    image_url = models.URLField()
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    amount_type = models.TextChoices('mass', 'volume')
    full_description = models.CharField(max_length=2000)

    def __str__(self):
        return f"{self.name}, id: {self.id}"
