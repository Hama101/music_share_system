from django.urls import path
from .views import RoomViex

urlpatterns = [
    path('', RoomViex.as_view() ),
]
