from django.shortcuts import render
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
