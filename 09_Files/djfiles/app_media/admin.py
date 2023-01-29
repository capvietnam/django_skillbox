from django.contrib import admin
from .models import File


class AvatarAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'description', 'created_at')
    list_display_links = ('id',)


admin.site.register(File, AvatarAdmin)
