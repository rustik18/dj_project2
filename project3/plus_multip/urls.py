from django.urls import path
from .views import add, multiply

urlpatterns = [
    path('add/<int:num1>/<int:num2>/', add),
    path('multiply/<int:num1>/<int:num2>/', multiply)
]