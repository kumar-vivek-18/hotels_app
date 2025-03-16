from user.models import User
from rest_framework import serializers

class UserProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_phone']

class UserProfileRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_name', 'user_email', 'user_gender', 'user_location', 'user_profile_image']