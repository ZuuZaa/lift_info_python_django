# Generated by Django 3.0.5 on 2020-04-17 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_auto_20200417_1757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='tetle_en',
            new_name='title_en',
        ),
    ]