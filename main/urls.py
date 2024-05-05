from django.urls import path
from .views import scan_qr_code,image_to_pdf

urlpatterns = [
    path('', scan_qr_code, name='scan_qr_code'),
    path("image_to_pdf/",image_to_pdf,name='image_to_pdf'),
]