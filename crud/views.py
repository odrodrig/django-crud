from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, welcome to my pretty CRUDdy app.")

# Create your views here.
