from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def login_view(request):
    return render(request,'login.html')

# Create your views here.
