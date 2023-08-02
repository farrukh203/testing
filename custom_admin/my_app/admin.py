from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from .models import Students, Course, Grade
from django.utils.html import format_html, mark_safe

admin.site.site_header = 'Admin Panel'
admin.site.index_title = 'Customization App'

#admin.ModelAdmin.actions_on_bottom = True
#admin.ModelAdmin.actions_on_top = False
#admin.ModelAdmin.actions_selection_counter = False

# Register your models here.
@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    #fieldsets = (
        #('Personal Information', {
        #    'fields': ('first_name', 'last_name', 'age', 'gender', 'address',
        #               'profile_image')
        #}),
        #('Education', {
        #    'fields': ('standard', 'course')
        #}),
        #('Parent Detail', {
        #    'fields': ('father_name', 'parent_contact_number')
        #})
    #)
    #list_display = ['first_name', 'last_name', 'gender', 'standard', 'average_show', 'stud_profile_pic']
    #exclude = ['first_name']
    #fields = [("first_name", "gender"), ("last_name", "standard")]
    #readonly_fields = ['first_name']
    search_fields = ("first_name__startswith",)

    def stud_profile_pic(self, obj):
        return mark_safe(f'<img src="profile/{obj.profile_image}" width="30" height="30" />')

    stud_profile_pic.short_description = "Profile Image"

    def average_show(self, obj):
        from django.db.models import Avg
        result = Grade.objects.filter(student=obj).aggregate(Avg("grade"))
        return result["grade__avg"]

    average_show.short_description = "Average"

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'view_student_link']
    list_filter = ("year",)

    def view_student_link(self, obj):
        count = obj.students_set.count()
        url = (reverse('admin:my_app_students_changelist')
               + '?'
               + urlencode({"course__id":f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Student </a>', url, count)

    view_student_link.short_description = "Student"


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass
