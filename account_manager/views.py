from django.shortcuts import render
import datetime
from .models import Cronograma, Estudiante

# Create your views here.
def account_balance(request):
  parent = request.user
  students = Estudiante.objects.all()
  
  filtered_students = list(filter(lambda student: student.padre.username == parent.username, students))
  payment_shedules = list(map(lambda student: (student.curso.cronograma, student), filtered_students))

  ctx = {
    'date': datetime.datetime.now().strftime('%B'),
    'estudiantes': filtered_students,
    'cronogramas': payment_shedules
  }
  return render(request, context=ctx, template_name='account_balance.html')

def get_account_balance(request):
  ctx = {
    'date': datetime.datetime.now().strftime('%B'),
    'cronograma': "",
  }
  try:
    print(request.user.username)
    cronograma = Cronograma.objects.get(user=request.user)
    ctx['cronograma'] = cronograma
  except:
    pass
  print(ctx)
  return render(request, context=ctx,template_name='base_balance.html')
