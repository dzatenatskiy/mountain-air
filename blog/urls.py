from django.urls import path
from django.urls import path

from .views import home, contact, gallery, rooms, standart_rooms, lux_rooms


urlpatterns = [
    path('', home),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery, name='gallery'),
    path('the-rooms/', rooms, name='rooms'),
    path('the-rooms/standart-family-room/', standart_rooms, name='standart_rooms'),    
    path('the-rooms/lux-family-room/', lux_rooms, name='lux_rooms'),
]