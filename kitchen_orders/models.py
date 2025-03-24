from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('preparing', 'En preparación'),
        ('ready', 'Lista'),
        ('delivered', 'Entregada'),
    ]

    customer_name = models.CharField(max_length=100)
    details = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Orden {self.id} - {self.customer_name} ({self.get_status_display()})"
