# Generated by Django 4.1.3 on 2023-04-11 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
