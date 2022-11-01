from django.db import models
from django.contrib.auth.models import User
from django.apps import apps


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, blank=True, verbose_name='Город')
    number = models.PositiveIntegerField(max_length=100, blank=True, verbose_name='Номер')
    verification = models.BooleanField(blank=True, verbose_name='Верификация')
    number_news = models.PositiveIntegerField(max_length=100, verbose_name='Коллчесво новостей')
