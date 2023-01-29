from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='profile',
                                verbose_name=_('user'))
    last_name = models.CharField(max_length=64, verbose_name=_('surname'), blank=True)
    description = models.CharField(max_length=64, verbose_name=_('About me'), blank=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True, verbose_name=_('avatar'))

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('user-profile', kwargs={'user': self.user})

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
        ordering = ['pk', 'user']
