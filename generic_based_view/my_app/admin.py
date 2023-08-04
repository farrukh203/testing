from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from .models import Students, Course, Grade
from django.utils.html import format_html, mark_safe

admin.site.site_header = 'Admin Panel'
admin.site.index_title = 'Customization App'

# Register your models here.


@admin.register(Students, Course, Grade)
class StudentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'age', 'gender', 'address', 'profile_image')
        }),
        ('Education', {
            'fields': ('standard', 'course')
        }),
        ('Parent Detail', {
            'fields': ('father_name', 'parent_contact_number')
        })
    )
    # readonly_fields = ['stu_created_at', 'stu_updated_at']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'year']


class GradeAdmin(admin.ModelAdmin):
    list_display = ['student', 'grade', 'course']
