from django.db import models
from ckeditor.fields import RichTextField

class Item(models.Model):
    image_file = models.ImageField(upload_to='images',blank=True)
    image_url = RichTextField()
    