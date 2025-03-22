from django.db import models
from model_utils import Choices
from django.utils.translation import gettext_lazy as _
# Create your models here.

class HotelAmenities(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        verbose_name = _('Hotel Amenity')


class Hotel(models.Model):
    HOTEL_CATEGORIES = Choices(
        (1,"ICY_YELLOW",_("ICY YELLOW")),
        (2,"ICY_WHITE",_("ICY WHITE")),
        (3,"ICY_BLACK",_("ICY BLACK")),
    )
    hotel_name = models.CharField(max_length=2048)
    hotel_description = models.TextField()
    hotel_email = models.EmailField(unique=True)
    hotel_phone = models.CharField(max_length=13, null=True, blank=True)
    hotel_owner = models.CharField(max_length=255)
    hotel_category = models.IntegerField(choices=HOTEL_CATEGORIES, default=HOTEL_CATEGORIES.ICY_YELLOW)
    hotel_address = models.CharField(max_length=2048)
    hotel_city = models.CharField(max_length=255)
    hotel_state = models.CharField(max_length=255)
    hotel_longitude = models.FloatField(verbose_name=_("Longitude"), null=True, blank=True, default=0.0)
    hotel_latitude = models.FloatField(verbose_name=_("Latitude"), null=True, blank=True, default=0.0)
    hotel_amenities = models.ManyToManyField(HotelAmenities)
    HOTEL_ACTIVE = Choices(
        ("UNVERIFIED",_("Unverified")),
        ("VERIFIED",_("Verified")),
        ("BLOCKED",_("Blocked"))
    )
    is_active = models.CharField(max_length=20, choices=HOTEL_ACTIVE, default=HOTEL_ACTIVE.UNVERIFIED)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        managed = True
        verbose_name = _("Hotels")


class HotelImages(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="hotel_image")
    image_url = models.ImageField(upload_to='media/hotel')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image id:{self.id}"

    class Meta:
        managed = True
        verbose_name = _("Hotel Images")

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    ROOM_CATEGORIES = Choices(
        (1,"ALPHA",_("Alpha")),
        (2,"BETA",_("Beta")),
        (3,"Gamma",_("Gamma")),
    )
    room_type = models.IntegerField(choices=ROOM_CATEGORIES, default=ROOM_CATEGORIES.ALPHA)
    room_description = models.TextField()
    room_price = models.IntegerField(default=0)
    room_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Room Description: {self.room_type}"
    
    class Meta:
        managed = True
        verbose_name = _("Hotel Room")
        indexes = [
            models.Index(fields=['hotel_id','room_type'])
        ]

class RoomAvailability(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    rooms_available = models.IntegerField(default=0)

    def __str__(self):
        return f"Room Availabily: {self.date} -> {self.rooms_available}"
    
    class Meta:
        managed = True
        verbose_name = _("Room Availability")
        indexes = [
            models.Index(fields=['date'])
        ]