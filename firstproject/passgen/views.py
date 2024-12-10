from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random
# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello world</h1> <br>,<h2> My first Django project!!</h2>')

def passgen1(request):
    char = list('abcdefghijklmnopqrstuvwxyz')
    password = ""
    for X in range(15):
        password += random.choice(char)

    pas = {'password': password}
    return JsonResponse(pas)