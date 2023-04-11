from django.contrib import admin
from .models import Profile, User, Sale


class UserAdmin(admin.ModelAdmin):
    """Панель админки пользователя"""
    list_display = ('id', 'password', 'username')
    list_display_links = ('id',)
    search_fields = ('login',)


class ProfileAdmin(admin.ModelAdmin):
    """Панель админки профиля пользователя"""
    list_display = ('id', 'balance')
    list_display_links = ('id',)
    search_fields = ('login',)


class SaleAdmin(admin.ModelAdmin):
    """Панель админки истории покупки"""
    list_display = ('id', 'user', 'goods', 'quantity', 'date')
    list_display_links = ('id',)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Sale, SaleAdmin)
