from django.db import models
from django.utils.translation import gettext_lazy as _


class House(models.Model):
    """Модель дома"""
    title = models.CharField(max_length=500, verbose_name=_('title'))
    type_house = models.ForeignKey('TypeHouse', on_delete=models.CASCADE, related_name='type', null=True)
    number_rooms = models.ForeignKey('NumberRooms', on_delete=models.CASCADE, related_name='quantity_rooms', null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = _('house')
        verbose_name_plural = _('house')
        ordering = ['title', 'type_house', 'number_rooms', 'price']

    def __str__(self):
        return self.title


class NumberRooms(models.Model):
    quantity = models.PositiveIntegerField(blank=True, default=0, verbose_name=_('quantity'))
    code = models.CharField(max_length=500, verbose_name=_('code'))


class TypeHouse(models.Model):
    name = models.CharField(max_length=500, verbose_name=_('name'))
    code = models.CharField(max_length=500, verbose_name=_('code'))
