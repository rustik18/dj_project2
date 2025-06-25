from django.shortcuts import render
from django.http import HttpResponse
import random


def random_number(request):
    nums = [i for i in range(0, 10)]
    return HttpResponse(f"Your random number is: {random.choice(nums)}")

def random_sequence(request):
    nums = [str(i) for i in range(0, 10)]
    random.shuffle(nums)
    return HttpResponse(f"Shuffled numbers: {"".join(nums)}")