from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello world</h1> <br>,<h2> My first Django project!!</h2>')