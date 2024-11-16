from django.contrib import admin

from . import models

# Register your models here.
@admin.register(models.School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)
