from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h4>Main message</h4>")

def about(request):
    return HttpResponse("<h4>Message about us</h4>")