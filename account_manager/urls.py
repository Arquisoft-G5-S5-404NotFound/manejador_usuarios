from django.urls import path

from . import views

urlpatterns = [
  path('', views.account_balance, name='account_balance'),
  path('payment_schedule/', views.payment_schedule, name='payment_schedule'),
  path('payment_schedule/<int:pk>', views.CronogramaUpdate.as_view(), name='payment_schedule')
]
