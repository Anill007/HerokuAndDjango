from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def helloworld(request):
    return render(request, "myapp/index.html")
