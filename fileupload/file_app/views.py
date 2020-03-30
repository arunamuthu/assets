from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import AssetSerializer

class AssetView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        asset_serializer = AssetSerializer(data=request.data)
        if asset_serializer.is_valid():
            asset_serializer.save()
            return Response(asset_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(asset_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
