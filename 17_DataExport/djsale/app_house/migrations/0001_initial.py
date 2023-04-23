# Generated by Django 4.1.3 on 2023-04-18 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='title')),
                ('type_house', models.CharField(max_length=500, verbose_name='type house')),
                ('number_rooms', models.PositiveIntegerField(blank=True, default=0, verbose_name='number rooms')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                'verbose_name': 'house',
                'verbose_name_plural': 'house',
                'ordering': ['title', 'type_house', 'number_rooms', 'price'],
            },
        ),
    ]
