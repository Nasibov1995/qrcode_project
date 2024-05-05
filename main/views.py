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
      
    try:
        url =  scanned_url

        options = webdriver.EdgeOptions()
        options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 1
        })
        
        driver = webdriver.Edge(options=options)
        
        driver.get(url)

        driver.maximize_window()
        
        time.sleep(2)

        # Click the button if need
        # download_image = driver.find_element(By.XPATH,"//*[@id='app-content-id']/div/div[1]/div[2]/button")

        # download_image.click()

        image = driver.find_element(By.XPATH,'//*[@id="app-content-id"]/div/div[1]/div[2]/div/img').get_attribute('src')
        
        
        
        Item(image_url=image).save()
      
        
    

    except:NoSuchElementException,AttributeError,NoSuchWindowException,WebDriverException

    return render(request, 'qrcode_scanner/scan.html')

