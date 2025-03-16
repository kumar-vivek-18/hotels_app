from django.shortcuts import render
from .serializers import UserProfileCreateSerializer, UserProfileRetrieveSerializer, UserProfileUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import User

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileCreateSerializer


class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileRetrieveSerializer
    lookup_field = 'user_phone'

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileUpdateSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = 'user_phone'

    def get_serializer(self, *args, **kwargs):
        if self.request.method == 'PATCH':
            kwargs['partial'] = True
        return super().get_serializer(*args,**kwargs)