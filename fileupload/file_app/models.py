from django.db import models
from .validators import validate_file_extension

class File(models.Model):
    file = models.FileField(blank=False, null=False, validators=[validate_file_extension])
    remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
