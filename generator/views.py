from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('Hello there friend')

def eggs(requests):
    return HttpResponse('<h1>I love eating eggs!</h1>')