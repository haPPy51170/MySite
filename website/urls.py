from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home_view, name='home'),

path("blog/<int:id>/", views.blog_detail, name="blog_detail_by_id"),
path("blog/<slug:slug>/", views.blog_detail, name="blog_detail_by_slug"),

    path('test/', views.test, name='test'),
]

