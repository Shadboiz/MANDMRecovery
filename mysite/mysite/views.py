from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from mysite.models import SiteEssentials


def index(request):
    site_essentials = SiteEssentials.objects.first()

    return render(request, "mysite/index.html", {"site_essentials": site_essentials})


def success(request):
    return render(
        request, "success.html", {"message": "Your message has been sent successfully!"}
    )
