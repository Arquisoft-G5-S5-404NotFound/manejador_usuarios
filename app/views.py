from django.shortcuts import render
from django.http import HttpResponse

from school_manager.logic import school_logic
from school_manager.models import Student

def app(request):
    schools_num = school_logic.get_schools().count()

    context = {
        'schools_num': schools_num,
        'students_num': Student.objects.all().count()
    }
    
    return render(request, context=context, template_name='index.html')

def health_check(request):
    return HttpResponse('ok')
