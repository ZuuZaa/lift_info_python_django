# Generated by Django 3.0.5 on 2020-04-28 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'İdarə', 'verbose_name_plural': 'İdarələr'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': 'Mütəxəssis', 'verbose_name_plural': 'Məsul şəxslər'},
        ),
        migrations.AlterField(
            model_name='department',
            name='address',
            field=models.CharField(max_length=250, verbose_name='ünvan'),
        ),
        migrations.AlterField(
            model_name='department',
            name='address_az',
            field=models.CharField(max_length=250, null=True, verbose_name='ünvan'),
        ),
        migrations.AlterField(
            model_name='department',
            name='address_en',
            field=models.CharField(max_length=250, null=True, verbose_name='ünvan'),
        ),
        migrations.AlterField(
            model_name='department',
            name='address_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='ünvan'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=250, verbose_name='idarənin adı'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name_az',
            field=models.CharField(max_length=250, null=True, verbose_name='idarənin adı'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name_en',
            field=models.CharField(max_length=250, null=True, verbose_name='idarənin adı'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='idarənin adı'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.Department', verbose_name='İdarə'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='email',
            field=models.CharField(max_length=150, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='full_name',
            field=models.CharField(max_length=250, verbose_name='Ad'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='full_name_az',
            field=models.CharField(max_length=250, null=True, verbose_name='Ad'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='full_name_en',
            field=models.CharField(max_length=250, null=True, verbose_name='Ad'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='full_name_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='Ad'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone_number',
            field=models.CharField(max_length=50, verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='role',
            field=models.CharField(max_length=150, verbose_name='Vəzifə'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='role_az',
            field=models.CharField(max_length=150, null=True, verbose_name='Vəzifə'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='role_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Vəzifə'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='role_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Vəzifə'),
        ),
    ]
