from django.shortcuts import render, HttpResponse
import datetime
from .models import Cronograma

# Create your views here.
def account_balance(request):
  ctx = {
    'date': datetime.datetime.now().strftime('%B'),
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
