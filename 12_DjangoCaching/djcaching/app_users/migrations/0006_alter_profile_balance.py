# Generated by Django 4.1.3 on 2023-02-11 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0005_alter_profile_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='balance'),
        ),
    ]