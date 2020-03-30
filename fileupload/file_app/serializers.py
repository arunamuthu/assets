from rest_framework import serializers
from .models import FileType,MimeType,FileMimeType,Type,TypeArea,Asset

class FileTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileType
        fields = "__all__"

class MimeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MimeType
        fields = "__all__"

class FileMimeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileMimeType
        fields = "__all__"

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"

class TypeAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeArea
        fields = "__all__"

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = "__all__"
