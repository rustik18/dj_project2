from django.shortcuts import render
from django.http import HttpResponse

def capitalize(request, text):
    return HttpResponse(text.upper())

def minimalize(request, text):
    return HttpResponse(text.lower())