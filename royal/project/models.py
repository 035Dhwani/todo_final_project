from django.db import models
from generic.models import BaseField
from royal.employee.models import User1

# Create your models here.
class Status(models.Model):
    status_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'status'

    def __str__(self):
        return self.status_name


class ProjectDetail(BaseField):
    project_title = models.CharField(max_length=50)
    project_description = models.CharField(max_length=250)
    project_technology = models.CharField(max_length=50)
    estimatedHours = models.IntegerField()
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)

    class Meta:
        db_table = 'project_detail'

    def __str__(self):
        return self.project_title


class ProjectTeam(BaseField):
    projectdetail =  models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)
    user1 =  models.ForeignKey(User1, on_delete=models.CASCADE)
    class Meta:
        db_table = 'project_team'

    def __str__(self):
        return self.projectdetail

    

class ProjectModule(BaseField):
     project_module_name = models.CharField(max_length=100)
     project_module_description = models.CharField(max_length=250)
     projectdetail_id =  models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)
     estimatedHours = models.IntegerField()
    
     class Meta:
         db_table = 'project_module'

class Priority(BaseField):
    priority_level = models.CharField(max_length=20)
    status =  models.ForeignKey(Status, on_delete=models.CASCADE)   

    class Meta:
        db_table = 'priority'
