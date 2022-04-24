from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "main/main.html")

def get_url(request, url_val):
    return render(request, "main/test.html", {
        "url_1": url_val[0],
    })

