from django.apps import AppConfig


class AdvertisementsConfig(AppConfig):
    name = 'Объявление'
    verbose_name = 'Объявления'


class AuthorConfig(AppConfig):
    name = 'Автор'
    verbose_name = 'Авторы'

class CategoryConfig(AppConfig):
    name = 'Категория'
    verbose_name = 'Категории'


