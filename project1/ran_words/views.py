from django.shortcuts import render
from django.http import HttpResponse
import random


def random_word(request):
    words = ['aloha', 'Hello', 'Bonjour', 'Ti amo', 'Arigato']
    random_item = random.choice(words)
    return HttpResponse(f"The random word: {random_item}")

def random_shifr(request):
    import string
    letters = list(string.ascii_lowercase)
    shifr = "".join(random.sample(letters, 6))
    return HttpResponse(shifr)