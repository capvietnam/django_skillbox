
from django.contrib import admin
from .models import Profile, User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'password', 'username')
    list_display_links = ('id',)
    search_fields = ('login',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'description', 'avatar')
    list_display_links = ('id',)
    search_fields = ('login',)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
