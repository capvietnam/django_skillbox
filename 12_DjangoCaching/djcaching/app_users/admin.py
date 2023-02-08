from django.contrib import admin
from .models import Profile, User, Purchase


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'password', 'username')
    list_display_links = ('id',)
    search_fields = ('login',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'balance')
    list_display_links = ('id',)
    search_fields = ('login',)


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'goods')
    list_display_links = ('id',)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Purchase, PurchaseAdmin)
