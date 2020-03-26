class Image(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='resized')

    def save(self):

        if not self.id and not self.image:
            return            

        super(Image, self).save()

        image = Image.open(self.image)
        (width, height) = image.size

        "Max width and height 800"        
        if (800 / width < 800 / height):
            factor = 800 / height
        else:
            factor = 800 / width

        size = ( width / factor, height / factor)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.image.path)