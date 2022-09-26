from django.contrib import admin
from .models import Advertisements, Author, Category


class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'price', 'date_create', 'date_close', 'author', 'views_count')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_filter = ('title',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Advertisements, AdvertisementsAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
