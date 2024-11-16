from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin

import datetime
from .models import Cronograma, Estudiante, PagoCronograma

# Create your views here.
def account_balance(request):
  parent = request.user
  students = Estudiante.objects.all()
  
  filtered_students = list(filter(lambda student: student.padre.username == parent.username, students))

  payment_shedules = list(map(lambda student: (student.curso.cronograma, student), filtered_students))
  
  # hay pagos para los cronogramas de pagos?
  payments = PagoCronograma.objects.filter(padre__username=parent.username)
  no_payments = Cronograma.objects.all().exclude(cronograma_id__in=list(map(lambda x: x.id, payments)))

  balance = 0
  for no_payment in no_payments:
    balance += no_payment.valor

  ctx = {
    'date': datetime.datetime.now().strftime('%B'),
    'estudiantes': filtered_students,
    'cronogramas': payment_shedules,
    'no_pagos': no_payments,
    'pagos': payments,
    'balance': balance
  }

  return render(request, context=ctx, template_name='account_balance.html')

def payment_schedule(request):
  cronogramas = Cronograma.objects.all()
  data = [
    {
      "id": cronograma.cronograma_id,
      "mes": cronograma.mes,
      "valor": cronograma.valor,
      "fecha_vencimiento": cronograma.fecha_vencimiento
    }
    for cronograma in cronogramas
  ]
  return JsonResponse(data, safe=False)

def payment_schedule_get(request, pk):
  cronograma_id = pk
  cronograma = Cronograma.objects.get(cronograma_id=cronograma_id)
  data = {
    "id": cronograma.cronograma_id,
    "mes": cronograma.mes,
    "valor": cronograma.valor,
    "fecha_vencimiento": cronograma.fecha_vencimiento
  }
  return JsonResponse(data)

class CronogramaUpdate(PermissionRequiredMixin, UpdateView):
  model = Cronograma
  fields = '__all__'
  template_name = 'update_cronograma.html'
  permission_required = 'cronograma.can_edit'