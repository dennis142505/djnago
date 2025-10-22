from django.contrib import admin
from django.urls import path, include
from greeting import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]
