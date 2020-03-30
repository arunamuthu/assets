from django.db import models
from .validators import validate_file_extension

class FileType(models.Model):
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

class MimeType(models.Model):
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

class FileMimeType(models.Model):
    file_type_id  = models.ForeignKey(FileType, related_name='id', on_delete=models.CASCADE)
    mime_type_id  = models.ForeignKey(MimeType, related_name='id', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Type(models.Model):
    type = models.CharField(max_length=20)
    file_type_id  = models.ForeignKey(FileMimeType, related_name='id', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class TypeArea(models.Model):
    typearea = models.CharField(max_length=20)
    height = models.FloatField()
    width = models.FloatField()
    type_id  = models.ForeignKey(Type, related_name='id', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class File(models.Model):
    name = models.FileField(blank=False, null=False, validators=[validate_file_extension])
    type_id  = models.ForeignKey(Type, related_name='id', on_delete=models.CASCADE)
    mime_type_id = models.ForeignKey(MimeType, related_name='id', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
