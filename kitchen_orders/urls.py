from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.order_list, name='order_list'),
    path('create/', views.order_create, name='order_create'),
    path('edit/<int:order_id>/', views.order_update, name='order_update'),
    path('delete/<int:order_id>/', views.order_delete, name='order_delete'),
]
