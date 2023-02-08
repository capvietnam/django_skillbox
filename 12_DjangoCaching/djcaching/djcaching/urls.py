from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('i18n', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path(r'goods/', include(r'app_goods.urls')),
    path(r'users/', include(r'app_users.urls')),
]
