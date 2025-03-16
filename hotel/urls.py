from django.urls import path
from .views import HotelCreateView

urlpatterns = [
    path('create/',HotelCreateView.as_view(), name = 'hotel-create')
]