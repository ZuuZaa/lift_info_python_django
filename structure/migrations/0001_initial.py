# Generated by Django 3.0.5 on 2020-04-24 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('name_az', models.CharField(max_length=250, null=True)),
                ('name_ru', models.CharField(max_length=250, null=True)),
                ('name_en', models.CharField(max_length=250, null=True)),
                ('address', models.CharField(max_length=250)),
                ('address_az', models.CharField(max_length=250, null=True)),
                ('address_ru', models.CharField(max_length=250, null=True)),
                ('address_en', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('full_name_az', models.CharField(max_length=250, null=True)),
                ('full_name_ru', models.CharField(max_length=250, null=True)),
                ('full_name_en', models.CharField(max_length=250, null=True)),
                ('role', models.CharField(max_length=150)),
                ('role_az', models.CharField(max_length=150, null=True)),
                ('role_ru', models.CharField(max_length=150, null=True)),
                ('role_en', models.CharField(max_length=150, null=True)),
                ('phone_number', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=150)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.Department')),
            ],
            options={
                'verbose_name_plural': 'Staff',
            },
        ),
    ]
