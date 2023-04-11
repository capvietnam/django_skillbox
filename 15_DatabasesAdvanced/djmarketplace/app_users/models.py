from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from app_goods.models import Goods
from django.utils import timezone


class Profile(models.Model):
    """
    Модель профиля пользователя
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='profile',
                                verbose_name=_('user'))
    balance = models.PositiveIntegerField(default=0, verbose_name=_('balance'), blank=True)
    money_spent = models.PositiveIntegerField(default=0, verbose_name=_('money_spent'), blank=True)

    def can_purchase_amount(self, amount):
        if amount <= self.balance:
            return True

    def update_balance(self, amount):
        self.balance += amount
        self.save()

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('user-profile', kwargs={'user': self.user})

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')
        ordering = ['pk', 'user']


class Sale(models.Model):
    """
    Модель истории покупок
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sale', verbose_name=_('user'))
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='sale', verbose_name=_('goods'))
    quantity = models.IntegerField(blank=True, default=0, verbose_name=_('quantity'))
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Sale')
        verbose_name_plural = _('Sale')
        ordering = ['pk', 'user', 'goods', 'quantity', 'date']
