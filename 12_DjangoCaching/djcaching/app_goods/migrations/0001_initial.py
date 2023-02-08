# Generated by Django 4.1.3 on 2023-01-31 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='title')),
            ],
            options={
                'verbose_name': 'shop',
                'verbose_name_plural': 'shops',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='title')),
                ('price', models.PositiveIntegerField(blank=True, verbose_name='price')),
                ('description', models.CharField(max_length=500, verbose_name='description')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='app_goods.shop', verbose_name='shop')),
            ],
            options={
                'verbose_name': 'goods',
                'verbose_name_plural': 'goods',
                'ordering': ['title', 'price', 'description', 'shop'],
            },
        ),
    ]
