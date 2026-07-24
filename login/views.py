from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def home_view(request):
    return render(request,'index.html')

def login_view(request):
    return render(request,'login.html')

# Create your views here.
