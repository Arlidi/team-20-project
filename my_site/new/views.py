from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from new.serializers import camera_deteil_serializer, camera_list_serializer
from new.models import camera

# Create your views here.

class camera_Create_View(generics.CreateAPIView):
    serializer_class = camera_deteil_serializer

class camera_list_view(generics.ListAPIView):
    serializer_class = camera_list_serializer
    queryset = camera.objects.all()

class camera_deteil_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = camera_deteil_serializer
    queryset = camera.objects.all()
