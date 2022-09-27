from django.db import models
from django.urls import reverse

class Advertisements(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Название')
    description = models.CharField(max_length=1000, blank=True, verbose_name='описание')
    price = models.FloatField(max_length=100, verbose_name='Цена')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_close = models.DateTimeField(verbose_name='Дата окончания')
    views_count = models.FloatField(max_length=100, verbose_name='Колличесво просмотров', blank=True)
    author = models.ForeignKey('Author', on_delete=models.PROTECT
                               , blank=True, verbose_name='Автор', related_name='advertisements')
    category = models.ForeignKey('Category', on_delete=models.PROTECT
                                 , blank=True, verbose_name='Категория', related_name='advertisements')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['title', 'date_create']


class Author(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Имя автора')
    number = models.IntegerField(max_length=100, verbose_name='Номер')
    email = models.CharField(max_length=150, verbose_name='Электронная почта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['name']


class Category(models.Model):
    title = models.CharField(max_length=1000, db_index=True, verbose_name='Наиминование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
