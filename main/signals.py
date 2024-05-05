from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.files.base import ContentFile
from . models import Item
import base64


@receiver(post_save, sender=Item)
def save_image_from_base64(sender, instance, created, **kwargs):
    if created and instance.image_url:
        # Decode base64 string
        base64_string = instance.image_url.split(",")[1]  # Assuming base64 string has a prefix like "data:image/jpeg;base64,"
        image_data = base64.b64decode(base64_string)

        # Save the image to the image_file field
        filename = "image.jpg"  # Or any other desired filename
        instance.image_file.save(filename, ContentFile(image_data), save=False)
        instance.save()
        
        return "Signals Worked"





