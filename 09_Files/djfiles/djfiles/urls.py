from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'blog/', include(r'app_blog.urls')),
    path(r'users/', include(r'app_users.urls')),
    path(r'file/', include(r'app_media.urls')),
]
