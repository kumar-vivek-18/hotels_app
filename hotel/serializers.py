from .models import HotelAmenities, HotelImages, Hotel
from rest_framework import serializers

class HotelAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelAmenities
        fields = ['id', 'name']


class HotelImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImages
        fields = ['id', 'image_url']

class HotelSerializer(serializers.ModelSerializer):
    hotel_amenities = HotelAmenitiesSerializer(many = True,required=False, read_only=True)
    hotel_images = HotelImagesSerializer(many = True, required=False, read_only=True)
    hotel_amenities = serializers.ListField(child=serializers.CharField(), write_only = True,required=False)
    hotel_images = serializers.ListField(child=serializers.ImageField(), write_only = True, required=False)

    class Meta:
        model = Hotel
        fields = [
            'id', 'hotel_name','hotel_description','hotel_email','hotel_phone', 'hotel_owner', 'hotel_category', 'hotel_address',
            'hotel_city', 'hotel_state', 'hotel_longitude', 'hotel_latitude',
            'hotel_amenities', 'hotel_images', 'is_active', 'created_at', 'updated_at'
        ]

    def create(self, validated_data):
        print("*****", validated_data)
        amenities_data = validated_data.pop('hotel_amenities',[])
        images_data = validated_data.pop('hotel_images',[])

        hotel = Hotel.objects.create(**validated_data)
        print("********* amenities", amenities_data)
        print("********** images", images_data)
        for amenity_data in amenities_data:
            if len(amenity_data)>0:
                amenity, _ = HotelAmenities.objects.get_or_create(name=amenity_data)
                hotel.hotel_amenities.add(amenity)

        for image_data in images_data:
            if image_data:
                image = HotelImages.objects.create(image_url=image_data)
                hotel.hotel_images.add(image)
        return hotel
