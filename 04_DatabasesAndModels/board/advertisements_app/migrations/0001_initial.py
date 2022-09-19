# Generated by Django 2.2 on 2022-09-19 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Имя автора')),
                ('number', models.IntegerField(max_length=100, verbose_name='Номер')),
                ('email', models.CharField(max_length=150, verbose_name='Электронная почта')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=1000, verbose_name='Наиминование категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Advertisements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Название')),
                ('description', models.CharField(blank=True, default='', max_length=1000, verbose_name='описание')),
                ('price', models.FloatField(default=0, max_length=100, verbose_name='Цена')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_close', models.DateTimeField(verbose_name='Дата окончания')),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='advertisements', to='advertisements_app.Author', verbose_name='Автор')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='advertisements', to='advertisements_app.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'ordering': ['title', 'date_create'],
            },
        ),
    ]
