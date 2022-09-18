from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class About(models.Model):
    
    description = models.TextField(verbose_name="Qısa mətn")
    content = models.TextField(verbose_name="Əsas mətn")

    class Meta:
        verbose_name = 'Məlumat'
        verbose_name_plural = 'Haqqımızda'

    def haqqında(self):
        return mark_safe(self.description_az)
        


    def __str__(self):
        return self.description
