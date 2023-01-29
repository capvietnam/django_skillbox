# Generated by Django 4.1.3 on 2023-01-29 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_media', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='file'),
        ),
        migrations.AlterField(
            model_name='file',
            name='description',
            field=models.TextField(blank=True, verbose_name='file'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='file', verbose_name='file'),
        ),
    ]
