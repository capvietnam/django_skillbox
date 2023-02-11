from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from app_goods.models import Goods


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='profile',
                                verbose_name=_('user'))
    balance = models.PositiveIntegerField(default=0, verbose_name=_('balance'), blank=True)
    # purchase_history = models.CharField(max_length=64, verbose_name=_('purchase history'), blank=True)

    def can_purchase_amount(self, amount):
        if amount <= self.balance:
            return True

    def input(self, amount):
        self.user_balance = self.user_balance + amount

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('user-profile', kwargs={'user': self.user})

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')
        ordering = ['pk', 'user']


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchase', verbose_name=_('user'))
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='purchase', verbose_name=_('goods'))

    class Meta:
        verbose_name = _('order_history')
        verbose_name_plural = _('order_history')
        ordering = ['pk', 'user', 'goods']


