from django.shortcuts import render, HttpResponse

# Create your views here.
def school(request):
  return HttpResponse('School Manager')