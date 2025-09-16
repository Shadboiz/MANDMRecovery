from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import mysite.views as views
import invoice.views as invoice_views


urlpatterns = [
    path("", views.index, name="index"),
    path("invoice/", invoice_views.invoice, name="invoice"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
