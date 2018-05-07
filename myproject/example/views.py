from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse("hello world!")


def hello_temp(request):
    return render(request,'hello.html')