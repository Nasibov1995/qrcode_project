# qrcode_scanner/views.py

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
        
        
        
        # with open('baza.txt','a') as file:
        #     file.write(image)

        
        time.sleep(4) 
        response = requests.get(image)
        image_data = response.content

        # Generate a PDF
        pdf_buffer = HttpResponse(content_type='application/pdf')
        pdf_buffer['Content-Disposition'] = f'attachment; filename="image_to_pdf.pdf"'

        c = canvas.Canvas(pdf_buffer, pagesize=letter)
        c.drawImage(image_data, inch, inch, width=400, height=300)
        c.save()
            
        
        
        # image_filename = download_image_from_url(image)

        # media_directory = settings.MEDIA_ROOT
        # shutil.move(image_filename, os.path.join(media_directory, 'downloaded_image.jpg'))
        
        # response = requests.get(image)
        # if response.status_code == 200:
        #     image_content = BytesIO(response.content)
        #     img = Image.open(image_content)
        #     my_model = Item()
        #     my_model.image_file.save('image.jpg', img)
        #     my_model.save()
        
        
        
        

    except:NoSuchElementException,AttributeError,NoSuchWindowException,WebDriverException

    return render(request, 'qrcode_scanner/scan.html')


def download_image_from_url(image_url):
    # Download the image using requests or any other method
    # Here, we'll assume the image is downloaded using requests
    # You may need to adjust this part based on your specific requirements
    import requests
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        image_filename = 'downloaded_image.jpg'
        with open(image_filename, 'wb') as f:
            f.write(image_response.content)
        return image_filename
    else:
        raise Exception("Failed to download image.")


   

