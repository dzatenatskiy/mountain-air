from django.urls import path
from django.urls import path

from .views import home, contact, gallery


urlpatterns = [
    path('', home),
    path('contact/', contact),
    path('gallery/', gallery),    
]