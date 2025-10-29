
from django.urls import path,include
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('counter/', views.counter_view, name='counter'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_page, name='login'),

]
