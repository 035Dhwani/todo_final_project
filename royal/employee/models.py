from django.db import models
from django.contrib.auth.models import  AbstractUser

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
