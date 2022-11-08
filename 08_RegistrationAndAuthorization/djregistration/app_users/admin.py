from django.contrib import admin
from .models import Profile


class Users(admin.ModelAdmin):
    list_display = ('id', 'user', 'city', 'number', 'number_news', 'verification',)
    list_display_links = ('id',)
    search_fields = ('login',)


admin.site.register(Profile, Users)
