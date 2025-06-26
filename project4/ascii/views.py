from django.shortcuts import render
from django.http import HttpResponse


def letter_by_ascii(request, num):
    return HttpResponse(chr(num))

def ascii_by_letter(request, chr):
    return HttpResponse(ord(chr))