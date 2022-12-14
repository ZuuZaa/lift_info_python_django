# Generated by Django 3.0.5 on 2020-04-19 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number_1', models.CharField(max_length=20)),
                ('phone_number_2', models.CharField(max_length=20)),
                ('tel_1', models.CharField(max_length=20)),
                ('tel_2', models.CharField(max_length=20)),
                ('fax_number', models.CharField(max_length=20)),
                ('fax', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=250)),
                ('address_map_link', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_name', models.CharField(max_length=150)),
                ('link_url', models.CharField(max_length=250)),
            ],
        ),
    ]
