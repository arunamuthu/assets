from django.db import models
from django.core.files import File
from PIL import Image as Img
from io import BytesIO


class Image(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='resized')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    bottom = models.IntegerField(null=True)
    right = models.IntegerField(null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.image:
            image = Img.open(BytesIO(self.image.read()))
            (width, height) = image.size
            if self.bottom:
                increasedValue = round((self.bottom /100) * height)
                factor = round((height / width) * increasedValue)
                size = (factor,increasedValue)
            elif self.right:
                increasedValue = round((self.right /100) * height)
                factor = round((height / width) * increasedValue)
                size = (increasedValue,factor)

            image = image.resize(size, Img.ANTIALIAS)
            output = BytesIO()
            image.save(output, format='JPEG', quality=75)
            output.seek(0)
            print(image.size)
            self.image = File(output, self.image.name)
        return  super(Image, self).save(*args, **kwargs)