from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        COCINERO = 'COCINERO', 'Cocinero'
        CLIENTE = 'CLIENTE', 'Cliente'

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='users_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='users_permissions_set',
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        super().save(*args, **kwargs)

class ClienteManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CLIENTE)

class Cliente(User):
    base_role = User.Role.CLIENTE

    cliente = ClienteManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Solo para Clientes"

class CocineroManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.COCINERO)

class Cocinero(User):
    base_role = User.Role.COCINERO

    cocinero = CocineroManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Solo para Cocineros"
