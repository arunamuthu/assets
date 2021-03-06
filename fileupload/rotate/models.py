from django.db import models
from django.core.files import File
from PIL import Image as Img
from io import BytesIO

class Image(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='rotated')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.image:
            pilImage = Img.open(BytesIO(self.image.read()))
            pilImage = pilImage.rotate(90, expand=True)
            print(pilImage)
            output = BytesIO()
            pilImage.save(output, format='JPEG', quality=75)
            output.seek(0)
            self.image = File(output, self.image.name)

        return super(Image, self).save(*args, **kwargs)