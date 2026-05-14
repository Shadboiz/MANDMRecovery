from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Location


class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0

    def items(self):
        return ["index"]

    def location(self, item):
        return reverse(item)


class LocationSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Location.objects.filter(is_active=True)

    def location(self, obj):
        return obj.seo_path
