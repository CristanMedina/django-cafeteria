from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Order
from .forms import OrderForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, 'kitchen_orders/home.html')

# Función para verificar si el usuario es administrador
def is_admin(user):
    return user.is_staff

# Lista de órdenes (solo administradores)
@login_required
@user_passes_test(is_admin)
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'kitchen_orders/order_list.html', {'orders': orders})

# Crear orden (solo clientes)
@login_required
def order_create(request):
    if request.user.is_staff:
        return redirect('home')  # Evita que administradores creen órdenes

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = OrderForm()

    return render(request, 'kitchen_orders/order_form.html', {'form': form})

# Editar orden (solo administradores)
@login_required
@user_passes_test(is_admin)
def order_update(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)

    return render(request, 'kitchen_orders/order_form.html', {'form': form})

# Eliminar orden (solo administradores)
@login_required
@user_passes_test(is_admin)
def order_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect('order_list')
