from django.db import models
from django.core.files import File
from PIL import Image as Img
from io import BytesIO


class Image(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='quality_reduced')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.image:
            image = Img.open(BytesIO(self.image.read()))
            output = BytesIO()
            image.save(output, format='JPEG',quality=20,optimize=True)
            output.seek(0)
            print(image.size)
            self.image = File(output, self.image.name)
        return  super(Image, self).save(*args, **kwargs)
