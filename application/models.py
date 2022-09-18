from django.db import models

# Create your models here.
class Application(models.Model):

    request_type = models.CharField(max_length=100, verbose_name = 'Müraciət növü')
    department = models.CharField(max_length=250, verbose_name = 'Struktur vahidi')
    subject = models.CharField(max_length=150, verbose_name = 'Müraciət mövzusu')
    first_name = models.CharField(max_length=150, verbose_name = 'Ad')
    last_name = models.CharField(max_length=150, verbose_name = 'Soyad')
    email = models.EmailField(max_length=200, verbose_name = 'E-mail')
    phone_number = models.CharField(max_length=20, verbose_name = 'Telefon')
    content = models.TextField( verbose_name = 'Müraciətin mətni')
    published = models.DateTimeField(auto_now_add=True, verbose_name = 'tarix')

    class Meta:
        verbose_name = 'Müraciət'
        verbose_name_plural = 'Elektron müraciətlər'

    def __str__(self):
        return self.request_type

class ApplicationSubject(models.Model):

    name = models.CharField(max_length=150, verbose_name = 'Mövzu')

    class Meta:
        verbose_name = 'Mövzu'
        verbose_name_plural = 'Müraciət mövzuları'

    def __str__(self):
        return self.name
