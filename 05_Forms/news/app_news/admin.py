from django.contrib import admin
from .models import News, Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date_create', 'date_update', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_filter = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'description', 'news')
    list_display_links = ('id', 'author')
    search_fields = ('author',)


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
