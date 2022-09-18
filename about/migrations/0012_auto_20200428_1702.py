# Generated by Django 3.0.5 on 2020-04-28 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0011_auto_20200421_1000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'Məlumat', 'verbose_name_plural': 'Haqqımızda'},
        ),
        migrations.AlterField(
            model_name='about',
            name='content',
            field=models.TextField(verbose_name='Əsas mətn'),
        ),
        migrations.AlterField(
            model_name='about',
            name='content_az',
            field=models.TextField(null=True, verbose_name='Əsas mətn'),
        ),
        migrations.AlterField(
            model_name='about',
            name='content_en',
            field=models.TextField(null=True, verbose_name='Əsas mətn'),
        ),
        migrations.AlterField(
            model_name='about',
            name='content_ru',
            field=models.TextField(null=True, verbose_name='Əsas mətn'),
        ),
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(verbose_name='Qısa mətn'),
        ),
        migrations.AlterField(
            model_name='about',
            name='description_az',
            field=models.TextField(null=True, verbose_name='Qısa mətn'),
        ),
        migrations.AlterField(
            model_name='about',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Qısa mətn'),
        ),
        migrations.AlterField(
            model_name='about',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Qısa mətn'),
        ),
    ]
