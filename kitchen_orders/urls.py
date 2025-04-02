from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas de órdenes
    path('', views.home, name='home'),
    path('list/', views.order_list, name='order_list'),
    path('create/', views.order_create, name='order_create'),
    path('edit/<int:order_id>/', views.order_update, name='order_update'),
    path('delete/<int:order_id>/', views.order_delete, name='order_delete'),
    
    # Rutas de login y logout
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
