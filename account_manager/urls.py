from django.urls import path

from . import views

urlpatterns = [
  path('', views.account_balance, name='account_balance'),
  path('balance/', views.get_account_balance, name='get_account_balance'),
]
