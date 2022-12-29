from django.urls import path
from django.urls import path

from .views import home, contact, gallery, rooms, standart_rooms, lux_rooms, about_us, pravila


urlpatterns = [
    path('', home),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery, name='gallery'),
    path('the-rooms/', rooms, name='rooms'),
    path('the-rooms/standart-family-room/', standart_rooms, name='standart_rooms'),    
    path('the-rooms/lux-family-room/', lux_rooms, name='lux_rooms'),
    path('about-us/', about_us, name='about_us'),
    path('pravila-prozhivania/', pravila, name='pravila')
]