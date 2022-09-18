from django.contrib import admin
from .models import About

# Register your models here.
@admin.register(About)
class About_Admin(admin.ModelAdmin):
    fields = ['description_az','description_ru','description_en','content_az','content_ru','content_en']
    list_display = ['haqqında']
