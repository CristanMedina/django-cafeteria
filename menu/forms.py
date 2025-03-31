from django import forms
from .models import Dish, Style

class StyleForm(forms.ModelForm):
    class Meta:
        model = Style
        fields = ['name', 'ingredients_text']  # Cambiar a ingredients_text
        widgets = {
            'ingredients_text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter ingredients separated by commas'}),
        }

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'price', 'available', 'style']