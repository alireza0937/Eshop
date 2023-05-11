from django.db import models
from account.models import User
from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField()
    payment_data = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def basket_total(self):
        user_orders = OrderDetails.objects.filter(order__user_id=self.user_id, order__is_paid=True)
        sum = 0
        for all_product in user_orders:
                sum += all_product.count * all_product.product.price
        return sum


class OrderDetails(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    final_price = models.IntegerField(null=True, blank=True)
    count = models.IntegerField()

    def get_total_price(self):
        return self.product.price * self.count

    def __str__(self):
        return str(self.product)
