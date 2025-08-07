from django.contrib import admin
from .models import SiteEssentials


@admin.register(SiteEssentials)
class SiteEssentialsAdmin(admin.ModelAdmin):
    list_display = ("headline", "subheadline", "cta")
