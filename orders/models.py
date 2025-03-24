from django.db import models
from django.contrib.auth import get_user_model
from menu.models import Dish

User = get_user_model()

class Order(models.Model):
    STATUS_CHOICES = (
        ('preparando', 'Preparando'),
        ('listo', 'Listo'),
        ('entregado', 'Entregado'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(Dish, through='OrderItem')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='preparando')
    created_at = models.DateTimeField(auto_now_add=True)
    receipt_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    special_request = models.TextField(blank=True, null=True)
