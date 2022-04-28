
from django import views
from django.contrib import admin
from django.urls import path,include
from royal.project import views
from royal.project.views import AddModule,ViewModule,DetailModule,DeleteModule,UpdateModule
from royal.project.views import AddTeam,ViewTeam






urlpatterns = [
    
    path('home/',views.index, name='home'),
    path('pie/',views.pie_chart, name='pie'),
    path('bar/',views.bar_chart, name='bar'),
    path('subscription/',views.subscription, name='subscription'),
    path('dashboard/',views.chart, name='dashboard'),
    path('main/',views.main),
    path('addtask/',AddModule.as_view(), name = 'addtask'),
    path('viewtask/',ViewModule.as_view(), name = 'viewtask'),
    path('<int:pk>/viewtask/',DetailModule.as_view(), name = 'detailtask'),
    path('<int:pk>/deletetask/',DeleteModule.as_view(), name='deletetask'),
    path('<int:pk>/updatetask/',UpdateModule.as_view(), name='updatetask'),
    path('contact/',views.contact, name='contact_us'),
    path('service/',views.service, name='service'),
    path('addteam/', AddTeam.as_view(), name = 'addteam'),
    path('viewteam/',ViewTeam.as_view(), name = 'viewteam'),


      

]