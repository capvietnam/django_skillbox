from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from app_news.models import News


class NewsSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return News.objects.all()

    def lastmod(self, obj):
        return obj.date


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['housing_list', 'about', 'contacts', 'news_list']

    def location(self, item):
        return reverse(item)
