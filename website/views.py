from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def home_view(request):
    return render(request,'home.html')

def about_view(request):
    return render(request,'about.html')

def login_view(request):
    return render(request,'login.html')

def web_view(request):
    return render(request,'index.html')
# Create your views here.
