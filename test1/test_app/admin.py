from django.contrib import admin
#from .models import Student
from .models import Place, Restaurant, Supplier
from .models import Person, Group, Membership

# Register your models here.
#@admin.register(Student)
@admin.register(Place, Restaurant, Supplier)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'customers']
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['name', 'age', 'group']


@admin.register(Person, Group, Membership)
class PersonAdmin(admin.ModelAdmin):
    pass
    #list_display = ['name', 'age']


class GroupAdmin(admin.ModelAdmin):
    list_display = ['group_name', 'members']


class MembershipAdmin(admin.ModelAdmin):
    list_display = ['person', 'group', 'date_joined', 'invite_reason']
