from django.urls import path
from . import views

urlpatterns = [
    path('', views.dish_list, name='menu_home'),
    path('dishes/', views.dish_list, name='dish_list'),
    path('dishes/create/', views.dish_create, name='dish_create'),
    path('dishes/<int:pk>/update/', views.dish_update, name='dish_update'),
    path('dishes/<int:pk>/delete/', views.dish_delete, name='dish_delete'),
    path('styles/', views.style_list, name='style_list'),
    path('styles/create/', views.style_create, name='style_create'),
    path('styles/<int:pk>/update/', views.style_update, name='style_update'),
    path('styles/<int:pk>/delete/', views.style_delete, name='style_delete'),
]