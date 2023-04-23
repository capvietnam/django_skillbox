from django.contrib.sitemaps import Sitemap
from .models import News


class NewsSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return News.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.date
