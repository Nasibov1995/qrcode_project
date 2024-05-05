from django.db import models
from ckeditor.fields import RichTextField

class Item(models.Model):
    image_file = models.FileField(upload_to='qr_code_files',blank=True)
    image_url = RichTextField()
    