from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Blog(models.Model):
    description = models.CharField(max_length=500)
    file = models.FileField()
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='Blog',
                             verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['date_create', 'description']

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})
