from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    """Модель магазина всех товаров"""
    title = models.CharField(max_length=500, verbose_name=_('title'))
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news')
        ordering = ['title', 'date']

    def __str__(self):
        return self.title
