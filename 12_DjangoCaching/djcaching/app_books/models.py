from django.db import models
from django.utils.translation import gettext_lazy as _
from isbn_field import ISBNField


class Author(models.Model):
    """Модель автора книг базы данных"""
    name = models.CharField(max_length=500, verbose_name=_('name'))
    last_name = models.CharField(max_length=500, verbose_name=_('last name'))
    date_birthday = models.DateField(verbose_name=_('date birthday'))

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('author')
        ordering = ['name', 'last_name', 'date_birthday']

    def __str__(self):
        return self.name


class Books(models.Model):
    """Модель книг базы данных"""
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', verbose_name=_('author'))
    title = models.CharField(max_length=500, verbose_name=_('title'))
    isbn = ISBNField(verbose_name='isbn', blank=True)
    description = models.CharField(max_length=500, verbose_name=_('description'))
    date_release = models.DateField(verbose_name=_('year release'))
    pages = models.PositiveIntegerField(verbose_name=_('pages'))

    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')
        ordering = ['author', 'title', 'isbn', 'description', 'date_release', 'pages']

    def __str__(self):
        return self.title
