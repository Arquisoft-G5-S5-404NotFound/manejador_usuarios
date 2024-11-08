from django.db import models
import uuid

# Create your models here.
class School(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)

class Course(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4)
    name = models.CharField(max_length=100, help_text='The name of the course')
    school_schedules = [
        ('JM', 'Jornada mañana'),
        ('JT', 'Jornada tarde'),
        ('JN', 'Jornada noche')
    ]
    school_schedule = models.CharField(
        max_length=2,
        choices=school_schedules,
        default='JM'
    )

class Student(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4)
    names = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    balance = models.DecimalField(decimal_places=0, max_digits=9)
    school = models.ForeignKey(
        'School',
        on_delete=models.DO_NOTHING
    )
    course = models.ForeignKey(
        'Course',
        on_delete=models.DO_NOTHING
    )