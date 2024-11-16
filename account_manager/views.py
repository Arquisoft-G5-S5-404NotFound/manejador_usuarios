from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def account_balance(request):
  ctx = {
    'date': datetime.datetime.now().strftime('%B'),
  }
  return render(request, context=ctx, template_name='account_balance.html')
