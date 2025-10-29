from django.contrib.auth import views as auth_views
from accounts.views import signup_view, counter_view
from django.urls import path,include
from accounts import views

urlpatterns = [
    path('accounts/',include('accounts.urls')),

]
