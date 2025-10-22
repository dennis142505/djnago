from django.contrib import admin
from django.urls import path
from greeting import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.greeting),        # form page
    path('result/', views.greeting), # result page
]
