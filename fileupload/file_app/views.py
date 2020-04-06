from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .models import Asset, Type, TypeArea
from .serializers import AssetSerializer, TypeSerializer, TypeAreaSerializer

class AssetView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self,request):
        if request.method == 'GET':
            assets = Asset.objects.all()
            serializer = AssetSerializer(assets, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            asset_serializer = AssetSerializer(data=request.data)
            if asset_serializer.is_valid():
                asset_serializer.save()
                return Response(asset_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(asset_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssetDetailView(APIView):

    def get_object(self, pk):
        try:
            return Asset.objects.get(pk=pk)
        except Asset.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        asset = self.get_object(pk)
        serializer = AssetSerializer(asset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        asset = self.get_object(pk)
        serializer = AssetSerializer(asset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        asset = self.get_object(pk)
        asset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TypeView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self,request):
        if request.method == 'GET':
            types = Type.objects.all()
            serializer = TypeSerializer(types, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            type_serializer = TypeSerializer(data=request.data)
            if type_serializer.is_valid():
                type_serializer.save()
                return Response(type_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(type_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TypeDetailView(APIView):

    def get_object(self, pk):
        try:
            return Type.objects.get(pk=pk)
        except Type.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        types = self.get_object(pk)
        serializer = TypeSerializer(types)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        types = self.get_object(pk)
        serializer = TypeSerializer(types, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        types = self.get_object(pk)
        types.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TypeAreaView(APIView):
    def get(self,request):
        if request.method == 'GET':
            typeAreas = TypeArea.objects.all()
            serializer = TypeAreaSerializer(typeAreas, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            type_area_serializer = TypeAreaSerializer(data=request.data)
            if type_area_serializer.is_valid():
                type_area_serializer.save()
                return Response(type_area_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(type_area_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TypeAreaDetailView(APIView):

    def get_object(self, pk):
        try:
            return TypeArea.objects.get(pk=pk)
        except TypeArea.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        typeArea = self.get_object(pk)
        serializer = TypeAreaSerializer(typeArea)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        typeArea = self.get_object(pk)
        serializer = TypeAreaSerializer(typeArea, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        typeArea = self.get_object(pk)
        typeArea.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)