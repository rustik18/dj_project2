from django.urls import path
from .views import yielder, backyield

urlpatterns = [
    path('iterate/<int:a>/', yielder),
    path('back/<int:a>', backyield),
]