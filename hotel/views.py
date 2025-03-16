from django.shortcuts import render

from rest_framework import generics
from .serializers import HotelSerializer
from .models import Hotel


class HotelCreateView(generics.CreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def post(self, request, *args, **kwargs):
        print("********* req data", request.data)
        return super().post(request, *args, **kwargs)