from django.db import models
from royal.project.models import ProjectModule,ProjectDetail,Priority
from royal.employee.models import User1
from generic.models import BaseField
# Create your models here.
class Task(BaseField):
    task_title = models.CharField(max_length=50)
    projectmodule_id =  models.ForeignKey(ProjectModule, on_delete=models.CASCADE)
    projectdetail_id =  models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)

    class Meta:
        db_table = 'task'

class UserTask(BaseField):
    user_id =  models.ForeignKey(User1, on_delete=models.CASCADE)  
    task_id =  models.ForeignKey(Task, on_delete=models.CASCADE)   
    priority_id =  models.ForeignKey(Priority, on_delete=models.CASCADE)  

    class Meta:
        db_table = 'user_task'

class SubTask(BaseField):
    subtask = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    time = models.IntegerField()   

    class Meta:
        db_table = 'sub_task'
