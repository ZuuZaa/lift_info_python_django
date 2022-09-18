from django.contrib import admin
from .models import Department, Staff

# Register your models here.
@admin.register(Department)
class Department_Admin(admin.ModelAdmin):
    fields = ['name_az','name_ru','name_en','address_az','address_ru','address_en']
    list_display = ['name_az','address_az']

@admin.register(Staff)
class Staff_Admin(admin.ModelAdmin):
    fields = ['department','full_name_az','full_name_ru','full_name_en','role_az','role_ru','role_en','phone_number','email']
    list_display = ['full_name_az','role_az','department']
