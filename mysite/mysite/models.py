from django.db import models


class SiteEssentials(models.Model):
    headline = models.CharField(max_length=255)
    subheadline = models.CharField(max_length=255, blank=True)
    cta = models.CharField("Call to Action", max_length=255, blank=True)

    def __str__(self):
        return self.headline
