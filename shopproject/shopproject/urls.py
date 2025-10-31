from django.contrib import admin
from django.urls import path
from shopapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('products/', views.product_list),         # GET & POST
    path('products/<int:id>/', views.product_detail),  # PUT & DELETE
]
