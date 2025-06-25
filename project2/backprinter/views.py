from django.shortcuts import render
from django.http import HttpResponse

def print_back(request, text):
    return HttpResponse(text[::-1])


def print_shuffle(request, text):
    from random import shuffle
    text = list(text)
    shuffle(text)
    return HttpResponse("".join(text))