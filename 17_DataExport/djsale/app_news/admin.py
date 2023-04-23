from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')
    search_fields = ('id', 'title', 'description')
    list_display_links = ('id', 'title',)
