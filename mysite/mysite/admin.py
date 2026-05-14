from django.contrib import admin
from .models import Location, SiteEssentials


@admin.register(SiteEssentials)
class SiteEssentialsAdmin(admin.ModelAdmin):
    list_display = ("headline", "subheadline", "cta")


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "location_type", "parent", "is_active", "is_featured")
    list_filter = ("location_type", "is_active", "is_featured")
    search_fields = ("name", "slug")
    fields = (
        "name",
        "slug",
        "location_type",
        "parent",
        "is_active",
        "is_featured",
        "meta_title",
        "meta_description",
    )
