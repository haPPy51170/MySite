from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('login/', views.login_view, name='login'),
    path('web/', views.web_view, name='web'),
]

