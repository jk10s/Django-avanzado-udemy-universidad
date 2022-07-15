from django.shortcuts import render
from django.http.response import HttpResponse 

# Create your views here.
def jks(request):
    return HttpResponse('hola como andas')