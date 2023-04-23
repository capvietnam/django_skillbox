from django.urls import path
from .views import *
from .sitemaps import StaticViewSitemap, NewsSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticViewSitemap,
    'news': NewsSitemap,
}

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),
    path('housing/', housing_list, name='housing_list'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
