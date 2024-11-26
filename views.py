from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sravani(request):
    return HttpResponse('<h1><marquee>my name is sravani i like dancing</h1><marquee>')