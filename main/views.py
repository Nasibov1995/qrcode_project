from django.shortcuts import render,redirect
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException,NoSuchElementException,NoSuchWindowException
from . models import Item
import time
from selenium import webdriver
from pdf2image import convert_from_path
import pytesseract

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






pytesseract.pytesseract.tesseract_cmd = r'D:\PyTesseract\tesseract.exe'

# Path to your PDF file
pdf_path = 'media/qr_code_files/image.pdf'

# Convert PDF to list of images
images = convert_from_path(pdf_path)

# Initialize an empty list to store words
words = []

x = ['COREK']
# Iterate through each image (page) and perform OCR
for image in images:
    # Perform OCR on the image
    text = pytesseract.image_to_string(image)

    # Split the text into words and add them to the list of words
    page_words = text.split()
    
    
    
    common_elements =  [ common for common in x if common in page_words]
    words.extend(common_elements)

# Print the extracted words
for word in words:
    print(word)