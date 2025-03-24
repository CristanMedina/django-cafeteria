from django.shortcuts import render, get_object_or_404, redirect
from .models import Ingredient, Dish, Style
from .forms import IngredientForm, DishForm, StyleForm

# Ingredient Views
def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'menu/ingredient_list.html', {'ingredients': ingredients})

def ingredient_create(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm()
    return render(request, 'menu/ingredient_form.html', {'form': form})

def ingredient_update(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'menu/ingredient_form.html', {'form': form})

def ingredient_delete(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('ingredient_list')
    return render(request, 'menu/ingredient_confirm_delete.html', {'ingredient': ingredient})

# Dish Views
def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'menu/dish_list.html', {'dishes': dishes})

def dish_create(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = DishForm()
    return render(request, 'menu/dish_form.html', {'form': form})

def dish_update(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = DishForm(instance=dish)
    return render(request, 'menu/dish_form.html', {'form': form})

def dish_delete(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    if request.method == 'POST':
        dish.delete()
        return redirect('dish_list')
    return render(request, 'menu/dish_confirm_delete.html', {'dish': dish})

def style_list(request):
    styles = Style.objects.all()
    return render(request, 'menu/style_list.html', {'styles': styles})

def style_create(request):
    if request.method == 'POST':
        form = StyleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('style_list')
    else:
        form = StyleForm()
    return render(request, 'menu/style_form.html', {'form': form})

def style_update(request, pk):
    style = get_object_or_404(Style, pk=pk)
    if request.method == 'POST':
        form = StyleForm(request.POST, instance=style)
        if form.is_valid():
            form.save()
            return redirect('style_list')
    else:
        form = StyleForm(instance=style)
    return render(request, 'menu/style_form.html', {'form': form})

def style_delete(request, pk):
    style = get_object_or_404(Style, pk=pk)
    if request.method == 'POST':
        style.delete()
        return redirect('style_list')
    return render(request, 'menu/style_confirm_delete.html', {'style': style})
