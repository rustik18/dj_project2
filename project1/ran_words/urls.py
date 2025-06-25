from django.urls import path
from .views import random_word, random_shifr

urlpatterns = [
    path('word/', random_word),
    path('shifr/', random_shifr),
]