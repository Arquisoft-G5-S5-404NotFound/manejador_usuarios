from django.contrib.auth.models import User
from django.db import connection

class UsuarioManager:
    def crear_usuario(self, username, email, password):
        """Crea un nuevo usuario."""
        usuario = User.objects.create_user(username=username, email=email, password=password)
        return usuario

    def actualizar_usuario(self, user_id, **datos):
        """Actualiza los datos de un usuario por su ID."""
        try:
            usuario = User.objects.get(id=user_id)
            for key, value in datos.items():
                setattr(usuario, key, value)
            usuario.save()
            return usuario
        except User.DoesNotExist:
            return None

    def eliminar_usuario(self, user_id):
        """Elimina un usuario por su ID."""
        try:
            usuario = User.objects.get(id=user_id)
            usuario.delete()
            return True
        except User.DoesNotExist:
            return False

    def obtener_usuarios_activos(self):
        """Obtiene todos los usuarios activos usando una consulta raw."""
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM auth_user WHERE is_active = 1")
            filas = cursor.fetchall()
        return filas

    def buscar_usuario_por_email(self, email):
        """Busca un usuario por su email usando una consulta raw."""
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM auth_user WHERE email = %s", [email])
            usuario = cursor.fetchone()
        return usuario
