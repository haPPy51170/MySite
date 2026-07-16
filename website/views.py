from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_view(request):
    return HttpResponse("<h1>Welcome to the home page! 🏠<h1>")

def about_view(request):
    return HttpResponse("<h1>Welcome to the about page! ℹ️<h1>")

def login_view(request):
    return HttpResponse("<h1>Welcome to the login page! 🔐<h1>")

# Create your views here.
