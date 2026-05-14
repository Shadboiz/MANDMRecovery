from .models import Location, SiteEssentials


def site_context(request):
    site_essentials = SiteEssentials.objects.first()
    featured_locations = list(
        Location.objects.filter(is_active=True, is_featured=True, parent__isnull=False).order_by("name")
    )
    return {
        "site_essentials": site_essentials,
        "featured_locations": featured_locations,
    }
