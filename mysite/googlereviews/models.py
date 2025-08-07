from django.db import models
from datetime import date


class GoogleReview(models.Model):
    review_id = models.CharField(max_length=255, unique=True, primary_key=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)  # Added missing field
    date = models.DateField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.review_id} - {self.author}"

    class Meta:
        ordering = ["-date"]

    @property
    def time_ago(self):
        if not self.date:
            return "Unknown date"
        delta = date.today() - self.date
        days = delta.days

        if days == 0:
            return "Today"
        elif days == 1:
            return "1 day ago"
        elif days < 7:
            return f"{days} days ago"
        elif days < 30:
            weeks = days // 7
            return f"{weeks} week{'s' if weeks > 1 else ''} ago"
        elif days < 365:
            months = days // 30
            return f"{months} month{'s' if months > 1 else ''} ago"
        else:
            years = days // 365
            return f"{years} year{'s' if years > 1 else ''} ago"
