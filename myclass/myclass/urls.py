from django.urls import path
from greeting import views

urlpatterns = [
    path('', views.greeting),
    path('result', views.greeting),
]

