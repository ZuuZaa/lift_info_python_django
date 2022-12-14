# Generated by Django 3.0.5 on 2020-04-28 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'Şəkil', 'verbose_name_plural': 'Şəkillər'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Xəbər', 'verbose_name_plural': 'Xəbərlər'},
        ),
        migrations.AlterField(
            model_name='images',
            name='img',
            field=models.ImageField(upload_to='news/', verbose_name='şəkil'),
        ),
        migrations.AlterField(
            model_name='images',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News', verbose_name='xəbər'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(verbose_name='xəbərin mətni'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content_az',
            field=models.TextField(null=True, verbose_name='xəbərin mətni'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content_en',
            field=models.TextField(null=True, verbose_name='xəbərin mətni'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content_ru',
            field=models.TextField(null=True, verbose_name='xəbərin mətni'),
        ),
        migrations.AlterField(
            model_name='news',
            name='published',
            field=models.DateTimeField(auto_now_add=True, verbose_name='tarix'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=200, verbose_name='xəbər başlığı'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title_az',
            field=models.CharField(max_length=200, null=True, verbose_name='xəbər başlığı'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='xəbər başlığı'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='xəbər başlığı'),
        ),
    ]
