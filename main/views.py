# qrcode_scanner/views.py

from django.shortcuts import render,redirect
from django.http import JsonResponse

def scan_qr_code(request):
    if request.method == 'POST':
        scanned_url = request.POST.get('scanned_url')
        # Process the scanned QR code data here
        # For demonstration purposes, let's just print the scanned data
        print("Scanned QR code data:", scanned_url)
        # You can add further processing logic here, such as saving to a database or performing some action
        # return redirect(scanned_url)
    return render(request, 'qrcode_scanner/scan.html')


