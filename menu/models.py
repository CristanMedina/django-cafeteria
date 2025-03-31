from django.db import models

class Style(models.Model):
    name = models.CharField(max_length=100)
    ingredients_text = models.TextField(blank=True, null=True)  


    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    style = models.ForeignKey(Style, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name