from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_house.urls')),
    path('news/', include('app_news.urls')),
]
