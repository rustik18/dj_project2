from django.urls import path
from .views import capitalize, minimalize

urlpatterns = [
    path('big/<str:text>', capitalize),
    path('small/<str:text>', minimalize)
]