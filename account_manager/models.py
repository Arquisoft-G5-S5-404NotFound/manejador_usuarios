from django.db import models
from datetime import datetime

def get_first_day_of_current_month():
  return datetime(datetime.now().year, datetime.now().month, 1)

# Create your models here.
class Cronograma(models.Model):
  id_cronograma = models.AutoField(primary_key=True)
  mes = models.DateField(default=get_first_day_of_current_month)
  valor = models.DecimalField(max_digits=10, decimal_places=0)
  fecha_vencimiento = models.DateField(default=datetime.now)

  def __str__(self):
    return f'{self.mes.strftime("%B")}'

class Curso(models.Model):
  id_curso = models.AutoField(primary_key=True)
  jornada = models.CharField(choices=[('M', 'Mañana'), ('T', 'Tarde'), ('N', 'Noche')], max_length=1)
  anio = models.IntegerField(default=datetime.now().year)
  grado = models.IntegerField()
  grupo = models.CharField(max_length=1, default='A')
  description = models.CharField(max_length=100)
  cronograma = models.ForeignKey(Cronograma, on_delete=models.CASCADE)

class Estudiante(models.Model):
  id_estudiante = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=100)
  apellido = models.CharField(max_length=100)
  curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
