# Generated by Django 3.0.5 on 2020-04-18 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_auto_20200417_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='content_en',
        ),
        migrations.RemoveField(
            model_name='about',
            name='content_ru',
        ),
        migrations.RemoveField(
            model_name='about',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='about',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='about',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='about',
            name='title_ru',
        ),
    ]
