from django.core.mail import send_mail
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from mysite.models import Location, SiteEssentials
from googlereviews.models import GoogleReview


def index(request):
    site_essentials = SiteEssentials.objects.first()
    google_reviews = GoogleReview.objects.all()[:9]
    glasgow = (
        Location.objects.filter(
            slug="glasgow",
            parent__isnull=True,
            location_type=Location.CITY,
            is_active=True,
        )
        .prefetch_related("children")
        .first()
    )
    glasgow_areas = glasgow.children.filter(is_active=True).order_by("name") if glasgow else []
    return render(
        request,
        "mysite/index.html",
        {
            "site_essentials": site_essentials,
            "reviews": google_reviews,
            "service_area_city": glasgow,
            "service_area_children": glasgow_areas,
        },
    )


def service_area(request, city_slug, area_slug=None):
    site_essentials = SiteEssentials.objects.first()

    try:
        city = Location.objects.get(
            slug=city_slug,
            parent__isnull=True,
            location_type=Location.CITY,
            is_active=True,
        )
    except Location.DoesNotExist as exc:
        raise Http404("Service area not found") from exc

    location = city
    if area_slug:
        try:
            location = Location.objects.get(
                slug=area_slug,
                parent=city,
                is_active=True,
            )
        except Location.DoesNotExist as exc:
            raise Http404("Service area not found") from exc

    service_area_children = city.children.filter(is_active=True).order_by("name")
    return render(
        request,
        "mysite/location_page.html",
        {
            "site_essentials": site_essentials,
            "service_area_city": city,
            "service_area_location": location,
            "service_area_children": service_area_children,
        },
    )


def success(request):
    return render(
        request, "success.html", {"message": "Your message has been sent successfully!"}
    )
