from django.urls import path
from .views import random_number, random_sequence


urlpatterns = [
    path('number/', random_number),
    path('sequence/', random_sequence)
]