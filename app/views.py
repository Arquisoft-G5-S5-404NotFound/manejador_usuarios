from django.shortcuts import render

def app(request):
    return render(request, template_name='index.html')
