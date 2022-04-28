from django.shortcuts import render
from django.views.generic.edit import CreateView
from royal.task.models import SubTask
from django.views.generic import ListView

# Create your views here.
class AddSubTask(CreateView):
    model = SubTask
    fields = ['subtask','description']
    template_name = 'royal/task/addsubtask.html'
    success_url = '/task/viewsubtask/'

class ViewSubTask(ListView):
    model = SubTask
    temp = model.objects.all() 
    context_object_name = 'temp'
    template_name = 'royal/task/viewsubtask.html'
    # ordering = ['id']
