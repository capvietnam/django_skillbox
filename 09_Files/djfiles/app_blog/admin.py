
from django.contrib import admin
from .models import Blog, Images


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'date_create', 'user',)
    list_display_links = ('id', 'description', 'date_create', 'user',)
    search_fields = ('description',)


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'image',)
    list_display_links = ('id', 'blog', 'image',)
    search_fields = ('blog',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Images, ImagesAdmin)
