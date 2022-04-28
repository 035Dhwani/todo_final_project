from django import views
from django.contrib import admin
from django.urls import path,include
from royal.task import views
from royal.task.views import AddSubTask,ViewSubTask

urlpatterns = [
    
   path('addsubtask/',AddSubTask.as_view(), name = 'addsubtask'),
   path('viewsubtask/',ViewSubTask.as_view(), name = 'viewsubtask'),
  

]