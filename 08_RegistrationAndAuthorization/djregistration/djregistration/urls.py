from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'news/', include(r'app_news.urls')),
    path(r'user/', include(r'app_users.urls')),
]
