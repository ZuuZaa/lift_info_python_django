from django.contrib import admin
from .models import FooterLink, Contact

# Register your models here.
@admin.register(FooterLink)
class FooterLink_Admin(admin.ModelAdmin):
    fields = ['link_name_az','link_name_ru','link_name_en','link_url']
    list_display = ['link_name_az','link_url']
    
@admin.register(Contact)
class Contact_Admin(admin.ModelAdmin):
    fields = ['phone_number_1','phone_number_2','fax_number','email','address_az','address_ru','address_en','address_map_link']
    list_display = ['email','phone_number_1','phone_number_2']