from django.shortcuts import render, get_object_or_404, redirect
from .models import Dish, Style
from .forms import DishForm, StyleForm

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
