
from django.shortcuts import render,redirect
from django.http import JsonResponse
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException,NoSuchElementException,NoSuchWindowException
import requests
from django.http import HttpResponse
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
from . models import Item
import os
import shutil
import time
from django.conf import settings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import urllib.request




def scan_qr_code(request):
    if request.method == 'POST':
        scanned_url = request.POST.get('scanned_url')
        # Process the scanned QR code data here 
        # For demonstration purposes, let's just print the scanned data
        print("Scanned QR code data:", scanned_url)
        # You can add further processing logic here, such as saving to a database or performing some action
        # return redirect(scanned_url)
    try:
        url =  'https://monitoring.e-kassa.gov.az/#/index?doc=BS8TEG2azn4D1g8wb9wMb8ySuQyiSjMLommWyH3Qw7WR'

        options = webdriver.EdgeOptions()
        options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 1
        })
        
        driver = webdriver.Edge(options=options)
        
        driver.get(url)

        driver.maximize_window()
        
        time.sleep(2)

        # download_image = driver.find_element(By.XPATH,"//*[@id='app-content-id']/div/div[1]/div[2]/button")

        # download_image.click()

        image = driver.find_element(By.XPATH,'//*[@id="app-content-id"]/div/div[1]/div[2]/div/img').get_attribute('src')
        
        
        
        Item(image_url=image).save()
      
        
    

    except:NoSuchElementException,AttributeError,NoSuchWindowException,WebDriverException

    return render(request, 'qrcode_scanner/scan.html')




   

def image_to_pdf(request):
    # Open the image file
    image_path = 'media/images/image.jpg'  # Replace with your image path
    image = Image.open(image_path)

    # Get image dimensions
    image_width, image_height = image.size

    # Create a BytesIO object to write PDF data
    pdf_buffer = BytesIO()

    # Create a PDF canvas
    pdf_canvas = canvas.Canvas(pdf_buffer, pagesize=(image_width, image_height))
    
    # Draw the image onto the PDF canvas
    pdf_canvas.drawImage(image_path, 0, 0, width=image_width, height=image_height)

    # Save the PDF canvas
    pdf_canvas.save()

    # Rewind the BytesIO object
    pdf_buffer.seek(0)

    # Create a Django HTTP response with PDF content
    response = HttpResponse(pdf_buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="image_to_pdf.pdf"'
    return response