from django.db import models
from django.utils.translation import gettext_lazy as _


class File(models.Model):
    file = models.FileField(upload_to='file', verbose_name=_('file'))
    description = models.TextField(blank=True, verbose_name=_('file'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('file'))

    class Meta:
        verbose_name = _('file')
        verbose_name_plural = _('files')
        ordering = ['created_at', 'description']
