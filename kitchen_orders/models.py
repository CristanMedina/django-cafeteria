from django.db import models
from orders.models import Order

class KitchenOrder(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Pedido para {self.order.id}"
