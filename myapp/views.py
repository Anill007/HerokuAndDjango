from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def helloworld(request):
    return render(request, "myapp/index.html")


def helloworld2(request):
    return render(request, "second.html")
