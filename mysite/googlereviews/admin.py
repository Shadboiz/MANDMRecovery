from django.contrib import admin
from .models import GoogleReview


@admin.register(GoogleReview)
class GoogleReviewAdmin(admin.ModelAdmin):
    list_display = ("author", "rating", "date", "body")
    list_filter = ("rating", "date")
    search_fields = ("author", "body")
