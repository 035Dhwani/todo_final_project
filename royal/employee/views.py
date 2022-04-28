from email import message
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render,redirect
from dataclasses import fields
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView
from royal.employee.forms import EmployeeForm
from royal.employee.models import User1
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from .models import User, Employee, Manager
from .forms import EmployeeForm


class AddUser(CreateView):
    model = User1
    fields = ['user_name', 'user_email', 'user_password', 'role_id']
    template_name = 'royal/user/adduser.html'
    success_url = '/user/viewuser/'

class ViewUser(ListView):
    model = User1 
    temp = model.objects.all() 
    context_object_name = 'temps'
    template_name = 'royal/user/viewuser.html'
    ordering = ['id']
    
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


class EmployeeSignUpView(CreateView):
    model = User
    form_class = EmployeeForm
    template_name = 'user/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  
        username=form.cleaned_data.get('username')
        password1 = form.cleaned_data.get('password1')
        dict = {'username':username, 'password1': password1}
        subject, from_email, to = 'subject', settings.EMAIL_HOST_USER, form.cleaned_data.get('email')
        html_content=render_to_string('user/email.html', dict)
        text_content = strip_tags(html_content)
        msg= EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()      
        return redirect('/garage/index')

def sign(request):
     return render(request, 'royal/user/signup.html')
def login(request):
     return render(request, 'royal/user/login.html')


