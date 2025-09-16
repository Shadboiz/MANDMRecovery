from django.urls import path
from .views import invoice, invoice_success

urlpatterns = [
    path('', invoice, name='invoice'),
    path('invoice_success/', invoice_success, name='invoice_success'),
]
