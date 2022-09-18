from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class FooterLink(models.Model):

    link_name = models.CharField(max_length=150, verbose_name = 'Linkin adı')
    link_url = models.CharField(max_length=250, verbose_name = 'Keçid üçün url')

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Keçid üçün linklər'

    def __str__(self):
        return self.link_name

class Contact(models.Model):

    phone_number_1 = models.CharField(max_length=20, verbose_name = 'əlaqə nömrəsi 1')
    phone_number_2 = models.CharField(max_length=20, verbose_name = 'əlaqə nömrəsi 2')
    tel_1 = models.CharField(max_length=20)
    tel_2 = models.CharField(max_length=20)
    fax_number = models.CharField(max_length=20, verbose_name = 'faks')
    fax = models.CharField(max_length=20)
    email = models.CharField(max_length=150, verbose_name = 'e-mail')
    address = models.CharField(max_length=250, verbose_name = 'ünvan')
    address_map_link = models.CharField(max_length=250, verbose_name = 'naviqasiya linki')

    class Meta:
        verbose_name = 'Kontakt'
        verbose_name_plural = 'Kontakt'

    def save(self):
        super(Contact, self).save()

        tel_1 = int(''.join(filter(str.isdigit, self.phone_number_1)))
        tel_1 = '+' + str(tel_1)
        self.tel_1 = tel_1

        tel_2 = int(''.join(filter(str.isdigit, self.phone_number_2)))
        tel_2 = '+' + str(tel_2)
        self.tel_2 = tel_2

        fax = int(''.join(filter(str.isdigit, self.fax_number)))
        fax = '+' + str(fax)
        self.fax = fax

        super(Contact, self).save()

    def __str__(self):
        return self.email
