from django.db import models
from .validators import validate_file_extension

class FileType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

class MimeType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

class FileMimeType(models.Model):
    id = models.AutoField(primary_key=True)
    file_type_id  = models.ForeignKey(FileType,on_delete=models.CASCADE)
    mime_type_id  = models.ForeignKey(MimeType,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Type(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)
    file_type_id  = models.ForeignKey(FileType,default=1,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class TypeArea(models.Model):
    id = models.AutoField(primary_key=True)
    typearea = models.CharField(max_length=20)
    height = models.FloatField()
    width = models.FloatField()
    type_id  = models.ForeignKey(Type,default=1,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Asset(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.FileField(blank=False, null=False, validators=[validate_file_extension])
    type_id  = models.ForeignKey(Type,default=1,on_delete=models.CASCADE)
    mime_type_id = models.ForeignKey(MimeType,default=1,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
