from django.contrib import admin

from .models import Cronograma, Curso, Estudiante, User

# Register your models here.
@admin.register(Cronograma)
class CronogramaAdmin(admin.ModelAdmin):
  list_display = ('mes', 'valor', 'fecha_vencimiento')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
  list_display = ('jornada', 'anio', 'grado', 'grupo', 'description', 'cronograma')

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
  list_display = ('nombre', 'apellido', 'curso')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  list_display = ('username', 'first_name', 'last_name', 'is_active', 'date_joined')
