from django.urls import path
from .views import letter_by_ascii, ascii_by_letter

urlpatterns = [
    path('chr/<int:num>/', letter_by_ascii),
    path('<str:chr>/', ascii_by_letter),
]