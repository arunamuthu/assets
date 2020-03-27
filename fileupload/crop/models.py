from django.db import models

class Image(models.Model):
    description = models.CharField(max_length=120)
    image = models.ImageField(upload_to='cropped')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    x = models.FloatField()
    y = models.FloatField()


    def save(self):      
        super(Image, self).save()

        image = Image.open(self.image)
        (width, height) = image.size

        x = self.x
        y = self.y
        w = width
        h = height
        cropped_image = image.crop((x, y, w+x, h+y))

        return cropped_image