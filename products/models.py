from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name}, {self.category}"


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
