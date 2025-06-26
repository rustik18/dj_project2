from django.urls import path
from .views import in_text, return_5text

urlpatterns = [
    path('in/<str:a>', in_text),
    path('5times/<str:text>', return_5text)
]