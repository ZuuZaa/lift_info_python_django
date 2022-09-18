from django.contrib import admin
from .models import News, Images
#from image_cropping import ImageCroppingMixin

# Register your models here.
@admin.register(News)
class News_Admin(admin.ModelAdmin):

    fields = ['title_az','title_ru','title_en','content_az','content_ru','content_en']
    list_display = ['title_az','published']
    readonly_fields = ['slug','published']

# Register your models here.
@admin.register(Images)
class Images_Admin(admin.ModelAdmin):

    list_display = ['news','foto']
    readonly_fields = ['foto']