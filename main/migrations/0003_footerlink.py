# Generated by Django 3.0.5 on 2020-04-19 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_auto_20200419_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_name', models.CharField(max_length=150)),
                ('link_url', models.CharField(max_length=250)),
            ],
        ),
    ]