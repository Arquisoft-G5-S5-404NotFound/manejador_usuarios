from django.contrib import admin

from . import models

# Register your models here.
@admin.register(models.School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'school_schedule')

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('names', 'surname', 'balance')
