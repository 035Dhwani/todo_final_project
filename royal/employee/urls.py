
from django import views
from django.contrib import admin
from django.urls import path,include
from royal.employee import views
from royal.employee.views import AddUser,ViewUser,DetailUser,DeleteUser,UpdateUser
from .views import mail,sign





urlpatterns = [
    
    # path('home/',views.index),
    # path('main/',views.main),
    path('mail/',views.mail, name = 'mail'),
    path('sign/',views.sign, name = 'sign'),
    path('login/',views.login, name = 'login'),
    path('adduser/',AddUser.as_view(), name = 'adduser'),
    path('viewuser/',ViewUser.as_view(), name = 'viewuser'),
    path('<int:pk>/viewuser/',DetailUser.as_view(), name = 'detailuser'),
    path('<int:pk>/deleteuser/',DeleteUser.as_view(), name='deleteuser'),
    path('<int:pk>/updateuser/',UpdateUser.as_view(), name='updateuser'),
   

    # path ('home/our-services.html/', AddModule.as_view(), name = 'add')
  

]