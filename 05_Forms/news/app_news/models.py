from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Название')
    description = models.CharField(max_length=50, verbose_name='Описание')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Реклама'
        verbose_name_plural = 'Рекламы'
        ordering = ['date_create', 'title']

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    description = models.CharField(max_length=50, db_index=True, verbose_name='Текст комментария')
    author = models.CharField(max_length=50, verbose_name='Автор')
    news = models.ForeignKey('News', on_delete=models.CASCADE, related_name='comments', verbose_name='Новость')

    def get_description(self):
        if len(self.description) >= 15:
            return self.description[:15] + '...'
        else:
            return self.description

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['author']

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})
