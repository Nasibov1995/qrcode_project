from django.db import models
from urllib.request import urlopen
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import urllib.request
import os
import base64
from PIL import Image
from io import BytesIO

# Base64 encoded string representing the image
base64_string = "/9j/4AAQSkZJRgABAQAAAQABAAD/"  # Your Base64 string here

# Decode the Base64 string
image_data = base64.b64decode(base64_string)

# Create a PIL Image object from the decoded image data
image = Image.open(BytesIO(image_data))

# Save the image as a JPEG file
image.save("image.jpg")

# Optional: Display the image
image.show()


class Item(models.Model):
    image_file = models.ImageField(upload_to='images',blank=True)
    image_url = models.URLField(null=True,max_length=5000000)

    
    
    def save(self, *args, **kwargs):
        """Store image locally if we have a URL"""

        if self.image_url and not self.image_file:
            result = urllib.request.urlretrieve(self.image_url)
            self.image_file.save(
                    os.path.basename(self.image_url),
                    File(open(result[0], 'rb'))
                    )
        super().save(*args, **kwargs)


