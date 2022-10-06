from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Название')
    description = models.CharField(max_length=50, verbose_name='Описание')
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    is_published = models.BooleanField(verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Реклама'
        verbose_name_plural = 'Рекламы'
        ordering = ['date_create', 'title']


class Comment(models.Model):
    description = models.CharField(max_length=50, db_index=True, verbose_name='Текст комментария')
    author = models.CharField(max_length=50)
    news = models.OneToOneField('News', on_delete=models.CASCADE, related_name='news')

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['author']
