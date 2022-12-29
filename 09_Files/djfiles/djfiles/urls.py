from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
                  path(r'admin/', admin.site.urls),
                  path(r'blog/', include(r'app_blog.urls')),
                  path(r'users/', include(r'app_users.urls')),
                  path(r'media/', include(r'app_media.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
