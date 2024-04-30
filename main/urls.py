from django.urls import path
from .views import scan_qr_code

urlpatterns = [
    path('', scan_qr_code, name='scan_qr_code'),
]