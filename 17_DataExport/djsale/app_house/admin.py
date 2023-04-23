from django.contrib import admin
from .models import House, NumberRooms, TypeHouse


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    search_fields = ('id', 'title', 'description',)
    list_display_links = ('id', 'title',)


@admin.register(TypeHouse)
class HouseTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')


@admin.register(NumberRooms)
class HouseTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantity', 'code')
