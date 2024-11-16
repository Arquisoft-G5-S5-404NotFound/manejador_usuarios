from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

def get_first_day_of_current_month():
  return datetime(datetime.now().year, datetime.now().month, 1)

# Create your models here.
class Cronograma(models.Model):
  cronograma_id = models.AutoField(primary_key=True)
  mes = models.DateField(default=get_first_day_of_current_month)
  valor = models.DecimalField(max_digits=10, decimal_places=0)
  fecha_vencimiento = models.DateField(default=datetime.now)

  def __str__(self):
    return f'{self.mes} - {self.fecha_vencimiento} - {self.valor}'

class Curso(models.Model):
  curso_id = models.AutoField(primary_key=True)
  jornada = models.CharField(choices=[('M', 'Mañana'), ('T', 'Tarde'), ('N', 'Noche')], max_length=1)
  anio = models.IntegerField(default=datetime.now().year)
  grado = models.IntegerField()
  grupo = models.CharField(max_length=1, default='A')
  description = models.CharField(max_length=100)
  cronograma = models.ForeignKey(Cronograma, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.jornada} - {self.anio} - {self.grado} - {self.grupo}'

class Estudiante(models.Model):
  estudiante_id = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=100)
  apellido = models.CharField(max_length=100)
  curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.nombre} {self.apellido}'

class User(AbstractUser):
  estudiante = models.ForeignKey(Estudiante, null=True, blank=True, on_delete=models.DO_NOTHING)

  def __str__(self):
    return f'{self.username} - {self.first_name} {self.last_name}'

  def save(self, *args, **kwargs):
    if not self.password.startswith('pbkdf2_sha256$'):
      self.password = make_password(self.password)
    super().save(*args, **kwargs)
