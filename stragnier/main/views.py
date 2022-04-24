from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Yep")

def get_url(request, url_val):
    return HttpResponse(f'url is {url_val}')