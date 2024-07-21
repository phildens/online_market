from user_buyer.models import CustomUser
from django.db import models
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id};  {self.user};  {str(self.date_ordered)}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    total = models.IntegerField(default=1)

    def __str__(self):
        return f"id: {self.id}; order_id: {self.order.id}; product: {self.product.name};  amount: {self.total};"


class PaymentDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=50)
    paid_status = models.BooleanField(default=False)
    cost = models.IntegerField(null=False)

    def __str__(self):
        return f"order_id: {self.order.id};  type: {self.payment_type}; status: {self.paid_status}"