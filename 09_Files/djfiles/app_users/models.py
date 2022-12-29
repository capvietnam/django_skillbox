from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='profile')
    last_name = models.CharField(max_length=64, verbose_name='Фамилия', blank=True)
    description = models.CharField(max_length=64, verbose_name='О себе', blank=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True, verbose_name='изображение')

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('user-profile', kwargs={'user': self.user})

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ['pk', 'user']
