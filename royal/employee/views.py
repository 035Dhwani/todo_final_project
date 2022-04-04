from email import message
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from dataclasses import fields
from multiprocessing import context
from pyexpat import model
from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView
from royal.employee.models import User1
from django.conf import settings
from django.core.mail import send_mail


class AddUser(CreateView):
    model = User1
    fields = ['user_name', 'user_email', 'user_password', 'role_id']
    template_name = 'royal/user/adduser.html'
    success_url = '/user/viewuser/'

class ViewUser(ListView):
    model = User1 
    temp = model.objects.all() 
    context_object_name = 'temp'
    template_name = 'royal/user/viewuser.html'
    
class DetailUser(DetailView):
    model = User1
    context_object_name = 'temp'
    template_name = 'royal/user/detailuser.html'

class DeleteUser(DeleteView):
    model = User1
    template_name = 'royal/user/deleteuser.html'
    success_url = '/user/viewuser/'

class UpdateUser(UpdateView):
    model = User1  
    fields = ['user_name', 'user_email', 'user_password', 'role_id']
    template_name = 'royal/user/updateuser.html'
    success_url = '/user/viewuser/'

def mail(request):
     subject = 'welcome to TODO app !!'
     message = 'hello guys..'
     email_from = settings.EMAIL_HOST_USER
     recipient_list = ['shreyabhat792@gmail.com', 'shweta18082000@gmail.com', 'dhwanipatel2412@gmail.com']
     send_mail(subject,message,email_from,recipient_list)
     
     return HttpResponse('mail sent..')
