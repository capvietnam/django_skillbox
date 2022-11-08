from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.apps import apps
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    city = models.CharField(max_length=100, blank=True, verbose_name='Город')
    number = models.PositiveIntegerField(blank=True, verbose_name='Номер')
    verification = models.BooleanField(default=False, verbose_name='Верификация')
    number_news = models.PositiveIntegerField(default=0, verbose_name='Коллчесво новостей')

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('user-profile', kwargs={'user': self.user})

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ['pk', 'user']
