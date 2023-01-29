from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Blog(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='Blog',
                             verbose_name=_('user'))
    description = models.CharField(max_length=500, verbose_name=_('description'))
    date_create = models.DateTimeField(auto_now_add=True, verbose_name=_('date create'))

    class Meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')
        ordering = ['date_create', 'description']

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})


class Images(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='Images', verbose_name=_('blog'))
    image = models.ImageField(upload_to='images/', blank=True, verbose_name=_('image'))

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')
        ordering = ['image']
