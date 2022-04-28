from django.db import models
from django.contrib.auth.models import  AbstractUser
from generic.models import BaseField
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'user_role'

    def __str__(self):
        return self.role_name
       

class User1(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=8)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE) 
    
    class Meta:
        db_table = 'end_user'
    
    def __str__(self):
        return self.user_name

class User(AbstractUser, BaseField):

    is_manager = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    profile_pic = models.ImageField(blank=True)

    phone_regex = RegexValidator(regex=r'^[6-9]{1}\d{9}', message="Phone number must be in 10 digit and starts from 6 to 9")
    phone_number = models.CharField(validators=[phone_regex],max_length=10, unique=True)

    address = models.TextField(max_length=500, blank=True)

    class Meta():
        db_table="User"

class Manager(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    mn_name= models.CharField(max_length=128, unique=True)
    mn_email = models.EmailField(max_length=128, unique=True)
    mn_address = models.TextField(max_length=100)

    class Meta():
        db_table="Manager"

    def __str__(self):
        return self.user.username

class Employee(models.Model):

    user= models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class Meta():
        db_table = 'Employee'

    def __str__(self):
        return self.user.username