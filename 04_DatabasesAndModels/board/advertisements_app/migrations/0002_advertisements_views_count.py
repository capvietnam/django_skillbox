# Generated by Django 2.2 on 2022-09-24 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisements',
            name='views_count',
            field=models.FloatField(blank=True, default=0, max_length=100, verbose_name='Колличесво просмотров'),
        ),
    ]
