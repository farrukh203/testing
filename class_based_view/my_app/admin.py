from django.contrib import admin
from .models import Students

# Register your models here.


@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['stu_name', 'stu_roll', 'stu_class']
