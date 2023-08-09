from django.contrib import admin
#from .models import Student
from .models import Place, Restaurant, Supplier

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
