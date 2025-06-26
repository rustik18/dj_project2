from django.shortcuts import render
from django.http import HttpResponse

def yielder(request, a):
    nums = []
    for i in range(0, a):
        nums.append(str(i))
    return HttpResponse("\n".join(nums))

def backyield(request, a):
    nums = []
    for i in range(a, 0, -1):
        nums.append(str(i))
    return HttpResponse("<br>".join(nums))