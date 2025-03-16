from django.urls import path
from .views import UserCreateView, UserRetrieveView, UserUpdateView

urlpatterns = [
    path('',UserCreateView.as_view(), name = 'user-create'),
    path('<str:user_phone>/',UserRetrieveView.as_view(), name = 'user-retrieve'),
    path('update/<str:user_phone>', UserUpdateView.as_view(), name = 'update-user-details')
]