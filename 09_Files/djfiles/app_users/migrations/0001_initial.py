# Generated by Django 4.1.3 on 2022-12-27 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=64, verbose_name='Фамилия')),
                ('description', models.CharField(blank=True, max_length=64, verbose_name='О себе')),
                ('avatar', models.ImageField(blank=True, upload_to='images/', verbose_name='изображение')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
                'ordering': ['pk', 'user'],
            },
        ),
    ]
