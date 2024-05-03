from django.db import models
from urllib.request import urlopen
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import urllib.request
import os


class Item(models.Model):
    image_file = models.ImageField(upload_to='images',blank=True)
    image_url = models.URLField(null=True)

    
    
    def cache(self):
        """Store image locally if we have a URL"""

        if self.image_url and not self.image_file:
            result = urllib.request.urlretrieve(self.image_url)
            self.image_file.save(
                    os.path.basename(self.image_url),
                    File(open(result[0], 'rb'))
                    )
            self.save()

    # def get_image_from_url(self, url):
    #     img_tmp = NamedTemporaryFile(delete=True)
    #     with urlopen(url) as uo:
    #         assert uo.status == 200
    #         img_tmp.write(uo.read())
    #         img_tmp.flush()
    #     img = File(img_tmp)
    #     self.image_file.save(img_tmp.name, img)
    #     self.image_url = url