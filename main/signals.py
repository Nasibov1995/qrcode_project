from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.files.base import ContentFile
from . models import Item
import base64
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.http import HttpResponse
from io import BytesIO

@receiver(post_save, sender=Item)
def save_image_from_base64(sender, instance, created, **kwargs):
    if created and instance.image_url:
        # Decode base64 string
        base64_string = instance.image_url.split(",")[1]  # Assuming base64 string has a prefix like "data:image/jpeg;base64,"
        image_data = base64.b64decode(base64_string)

        # Save the image to the image_file field
        # filename = "image.jpg"  # Or any other desired filename
        # instance.image_file.save(filename, ContentFile(image_data), save=False)
        # instance.save()
        
        # Open the image using PIL
        img = Image.open(BytesIO(image_data))

        # Create a PDF file
        pdf_buffer = BytesIO()
        c = canvas.Canvas(pdf_buffer, pagesize=letter)
        c.setPageSize((img.width, img.height))  # Set page size to match image size
        c.drawInlineImage(img, 0, 0)  # Draw the image at (0,0)
        c.save()

        # Save the PDF buffer to the image_file field
        filename_pdf = "image.pdf"  # Or any other desired filename for PDF
        instance.image_file.save(filename_pdf, ContentFile(pdf_buffer.getvalue()), save=True)

        

     
        
    return "Signals Worked"





