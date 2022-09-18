from django.contrib import admin
from .models import Application, ApplicationSubject

# Register your models here.
@admin.register(Application)
class Application_Admin(admin.ModelAdmin):
    list_display = ['request_type','content']
    readonly_fields = ['first_name','last_name','request_type','department','subject','content','email','phone_number','published']
    list_filter = ['request_type','department','subject']

@admin.register(ApplicationSubject)
class ApplicationSubject_Admin(admin.ModelAdmin):
   fields = ['name_az','name_ru','name_en']

