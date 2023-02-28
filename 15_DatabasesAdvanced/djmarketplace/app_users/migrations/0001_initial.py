# Generated by Django 4.1.3 on 2023-02-21 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_goods', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='app_goods.goods', verbose_name='goods')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'order_history',
                'verbose_name_plural': 'order_history',
                'ordering': ['pk', 'user', 'goods'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.PositiveIntegerField(blank=True, default=0, verbose_name='balance')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
                'ordering': ['pk', 'user'],
            },
        ),
    ]