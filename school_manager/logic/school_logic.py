from ..models import School

def get_schools():
    return School.objects.all()

def get_one_school(school_id):
    return School.objects.all().filter(id=school_id)