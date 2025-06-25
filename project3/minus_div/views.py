from django.shortcuts import render
from django.http import HttpResponse

def minus(request, num1, num2):
    resp = f"{num1} - {num2} = {num1-num2}"
    return HttpResponse(resp)

def divide(request, num1, num2):
    resp = f"{num1} / {num2} = {num1/num2}"
    return HttpResponse(resp)