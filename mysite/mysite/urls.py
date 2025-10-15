from django.urls import path
from greeting import views

urlpatterns = [
    path('home', views.greeting),
     path('about', views.greeting),
]
