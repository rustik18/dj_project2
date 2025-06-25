from django.shortcuts import render
from django.http import HttpResponse

def print_surname(request):
    return HttpResponse("surname:\tQosimjonov")

def print_age(request):
    return HttpResponse("age: 18")