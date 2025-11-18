from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth
from shortener import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('signup/', views.signup, name='signup'),
     path('login/', auth.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('', views.list_urls, name='list_urls'),
    path('add/', views.add_url, name='add_url'),
    path('edit/<int:id>/', views.edit_url, name='edit_url'),
    path('delete/<int:id>/', views.delete_url, name='delete_url'),

    path('<str:short>/', views.go, name='go'),
]
