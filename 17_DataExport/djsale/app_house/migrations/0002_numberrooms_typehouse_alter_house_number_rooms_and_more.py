# Generated by Django 4.1.3 on 2023-04-21 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_house', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumberRooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(blank=True, default=0, verbose_name='quantity')),
                ('code', models.CharField(max_length=500, verbose_name='code')),
            ],
        ),
        migrations.CreateModel(
            name='TypeHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='name')),
                ('code', models.CharField(max_length=500, verbose_name='code')),
            ],
        ),
        migrations.AlterField(
            model_name='house',
            name='number_rooms',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quantity_rooms', to='app_house.numberrooms'),
        ),
        migrations.AlterField(
            model_name='house',
            name='type_house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type', to='app_house.typehouse'),
        ),
    ]
