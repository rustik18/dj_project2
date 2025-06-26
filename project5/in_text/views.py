from django.shortcuts import render
from django.http import HttpResponse

def in_text(request, a):
    text = 'I love  working out! It feels so amazing when you\'re stretching to your limits!'
    if a in text:
        return HttpResponse(bool(True))
    else:
        return HttpResponse(bool(False))


def return_5text(request, text):
    return HttpResponse(text * 5)