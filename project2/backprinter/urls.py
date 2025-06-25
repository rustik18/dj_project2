from django.urls import path
from .views import print_back, print_shuffle

urlpatterns = [
    path('back/<str:text>', print_back),
    path('shuffle/<str:text>', print_shuffle)
]