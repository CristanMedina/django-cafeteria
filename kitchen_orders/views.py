from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import OrderForm

def home(request):
    return render(request, 'kitchen_orders/home.html')

# Listar órdenes
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'kitchen_orders/order_list.html', {'orders': orders})

# Crear orden
def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'kitchen_orders/order_form.html', {'form': form})

# Editar orden (sin restricciones de estado)
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

# Eliminar orden
def order_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect('order_list')
