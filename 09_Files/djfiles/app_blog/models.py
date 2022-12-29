from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Blog(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='Blog',
                             verbose_name='Пользователь')
    files = models.FileField(upload_to='file')
    description = models.CharField(max_length=500)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['date_create', 'description']

    # def __str__(self):
    #     return self.user.username

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})


class File(models.Model):
    file = models.FileField(upload_to='file')
