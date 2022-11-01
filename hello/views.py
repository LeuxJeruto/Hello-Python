from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello world!")

def leucrecia(request):
    return HttpResponse("Hello Leucrecia, you are doing it. Keep it up!")

def david(request):
    return HttpResponse("Hello David!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")