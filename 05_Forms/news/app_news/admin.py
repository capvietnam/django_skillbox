from django.contrib import admin
from .models import News, Comment, User


def make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)


make_published.short_description = "Mark selected stories as published"


def move_to_draft(modeladmin, request, queryset):
    queryset.update(is_published=False)


move_to_draft.short_description = "Mark selected stories as draft"


def remove_comment(modeladmin, request, queryset):
    queryset.update(description='Удалено администратором')


move_to_draft.short_description = "Delete Comments"


class CommentInline(admin.TabularInline):
    model = Comment

    def get_extra(self, request, obj=None, **kwargs):
        extra = 0
        return extra


class NewsAdmin(admin.ModelAdmin):
    inlines = [CommentInline, ]
    list_display = ('id', 'title', 'date_create', 'date_update', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_filter = ('is_published',)
    list_editable = ('is_published',)
    actions = [make_published, move_to_draft]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'get_description', 'news')
    list_display_links = ('id', 'author')
    search_fields = ('author',)
    list_filter = ('author',)
    list_display_links = ('id', 'author',)
    actions = [remove_comment]


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
