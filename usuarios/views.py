# usuarios/views.py

from django.shortcuts import render, redirect
from .forms import UsuarioForm
from django.http import JsonResponse
from usuarios.managers import UsuarioManager
from .managers import UsuarioManager

# Instancia del manejador
usuario_manager = UsuarioManager()

def crear_usuario(request):
    """Vista para crear un nuevo usuario usando el formulario."""
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()  # Crea el usuario en la base de datos
            return JsonResponse({'status': 'Usuario creado con éxito'})
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/crear_usuario.html', {'form': form})

def actualizar_usuario(request, user_id):
    # Supón que los datos vienen de una solicitud POST
    datos = {
        'email': request.POST.get('email'),
        'first_name': request.POST.get('first_name'),
        'last_name': request.POST.get('last_name')
    }
    usuario = usuario_manager.actualizar_usuario(user_id, **datos)
    if usuario:
        return JsonResponse({'usuario_id': usuario.id, 'username': usuario.username})
    else:
        return JsonResponse({'error': 'Usuario no encontrado'}, status=404)

def eliminar_usuario(request, user_id):
    exito = usuario_manager.eliminar_usuario(user_id)
    if exito:
        return JsonResponse({'status': 'Usuario eliminado'})
    else:
        return JsonResponse({'error': 'Usuario no encontrado'}, status=404)

def lista_usuarios_activos(request):
    usuarios = usuario_manager.obtener_usuarios_activos()
    return JsonResponse({'usuarios': usuarios})

def detalle_usuario_por_email(request, email):
    usuario = usuario_manager.buscar_usuario_por_email(email)
    if usuario:
        return JsonResponse({'usuario': usuario})
    else:
        return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
