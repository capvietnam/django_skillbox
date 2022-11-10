from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.apps import apps
from django.urls import reverse
from app_news.models import News


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    city = models.CharField(max_length=100, blank=True, verbose_name='Город')
    number = models.PositiveIntegerField(blank=True, verbose_name='Номер')
    verification = models.BooleanField(default=False, verbose_name='Верификация')
    can_news = models.BooleanField(default=False, verbose_name='Способность публиковать новости')

    @property
    def number_news(self):
        summ = 0
        for _ in self.user.News.filter(is_published=True):
            summ += 1
        return summ

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('user-profile', kwargs={'user': self.user})

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ['pk', 'user']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
