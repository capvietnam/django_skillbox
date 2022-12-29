from django.contrib import admin
from .models import Blog, User


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'files', 'date_create',  'user',)
    list_display_links = ('id', 'description', 'date_create', 'user',)
    search_fields = ('description', )



admin.site.register(Blog, BlogAdmin)
