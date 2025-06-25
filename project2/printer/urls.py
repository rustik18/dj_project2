from django.urls import path
from .views import print_age, print_surname

urlpatterns = [
    path('age/', print_age),
    path('surname/', print_surname)
]
