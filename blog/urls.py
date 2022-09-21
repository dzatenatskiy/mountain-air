from django.urls import path
from django.urls import path

from .views import home, contact, gallery


urlpatterns = [
    path('', home),
    path('контакты/', contact),
    path('галерея/', gallery),    
]