from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from your_app.models import Orden  # Reemplaza 'your_app' con el nombre de tu aplicación

def run():
    # Crear grupo de Clientes
    clientes_group, created = Group.objects.get_or_create(name='Clientes')

    # Crear grupo de Administradores
    admin_group, created = Group.objects.get_or_create(name='Administradores')

    # Asignar permisos al grupo de Administradores
    content_type = ContentType.objects.get_for_model(Orden)
    permisos = Permission.objects.filter(content_type=content_type)
    admin_group.permissions.set(permisos)

    print("Grupos y permisos configurados correctamente.")