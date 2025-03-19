from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import HotelInputSerializer, HotelOutputSerializer
from .models import Hotel


class HotelCreateView(generics.CreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelInputSerializer

    def create(self, request, *args, **kwargs):
        input_serializer = self.get_serializer(data = request.data)
        input_serializer.is_valid(raise_exception = True)
        hotel = input_serializer.save()
        
        output_serailizer = HotelOutputSerializer(hotel)
        headers = self.get_success_headers(output_serailizer.data)
        return Response(output_serailizer.data, status=status.HTTP_201_CREATED, headers=headers)
