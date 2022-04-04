
from django.contrib import admin
from django.urls import path,include
from product import views

urlpatterns = [
    path('addProduct/', views.addProduct),
    path('viewProduct/', views.viewProduct),

]