from django.db import models

# Create your models here.
class Department(models.Model):

    name = models.CharField(max_length=250, verbose_name = 'idarənin adı')
    address = models.CharField(max_length=250, verbose_name = 'ünvan')

    class Meta:
        verbose_name = 'İdarə'
        verbose_name_plural = 'İdarələr'

    def __str__(self):
        return self.name


class Staff(models.Model):

    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name = 'İdarə')
    full_name = models.CharField(max_length=250, verbose_name = 'Ad')
    role  = models.CharField(max_length=150, verbose_name = 'Vəzifə')
    phone_number = models.CharField(max_length=50, verbose_name = 'Telefon')
    tel = models.CharField(max_length=50)
    email = models.CharField(max_length=150, verbose_name = 'E-mail')

    class Meta:
        verbose_name = 'Mütəxəssis'
        verbose_name_plural = 'Məsul şəxslər'
        
    def save(self):
        super(Staff, self).save()
        tel = int(''.join(filter(str.isdigit, self.phone_number)))
        tel = '+' + str(tel)
        self.tel = tel
        super(Staff, self).save()

    def __str__(self):
        return self.full_name