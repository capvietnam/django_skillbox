from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('advertisement.urls')),
    path('python_basic', include('advertisement.urls')),
    path('django', include('advertisement.urls')),
    path('python_advanced', include('advertisement.urls')),
    path('SQL', include('advertisement.urls')),
    path('web_layout', include('advertisement.urls')),
]
