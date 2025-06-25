from django.urls import path
from .views import minus, divide

urlpatterns = [
    path('divide/<int:num1>/<int:num2>/', divide),
    path('minus/<int:num1>/<int:num2>/', minus)
]