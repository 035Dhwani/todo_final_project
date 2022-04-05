
from dataclasses import fields
from msilib.schema import ListView
from multiprocessing import context
from pyexpat import model
from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import DetailView,ListView
from royal.project.models import ProjectDetail, ProjectTeam



# Create your views here.
def index(request):
     return render(request, 'royal/index.html')
def main(request):
     return render(request, 'royal/home.html')
def contact(request):
     return render(request, 'royal/contact.html')
def service(request):
     return render(request, 'royal/service.html')
def pie_chart(request):
    lables = []
    data = []

    queryset = ProjectDetail.objects.all()[:5]
    for i in queryset:
        lables.append(i.project_title)
        data.append(i.estimatedHours)

    return render(request, 'royal/pie_chart.html',
        {
        'labels': lables,
        'data': data,

        })

class AddModule(CreateView):
    model = ProjectDetail
    fields = ['project_title', 'project_description', 'project_technology', 'estimatedHours', 'status_id']
    template_name = 'royal/task/addtask.html'
    success_url = '/project/viewtask/'

class ViewModule(ListView):
    model = ProjectDetail 
    temp = model.objects.all() 
    context_object_name = 'temps'
    template_name = 'royal/task/viewtask.html'
    
class DetailModule(DetailView):
    model = ProjectDetail
    context_object_name = 'temp'
    template_name = 'royal/task/detailtask.html'

class DeleteModule(DeleteView):
    model = ProjectDetail
    template_name = 'royal/task/deletetask.html'
    success_url = '/project/viewtask/'

class UpdateModule(UpdateView):
    model = ProjectDetail  
    fields = ['project_title', 'project_description', 'project_technology', 'estimatedHours', 'status_id']
    template_name = 'royal/task/updatetask.html'
    success_url = '/project/viewtask/'

class AddTeam(CreateView):
    model =  ProjectTeam
    fields = ['projectdetail', 'user1']
    template_name = 'royal/team/addteam.html'
    success_url = '/project/viewteam/'

class ViewTeam(ListView):
    model = ProjectTeam
    temp = model.objects.all() 
    context_object_name = 'temps'
    template_name = 'royal/team/viewteam.html'