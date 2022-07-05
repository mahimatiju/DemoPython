from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from  .models import task
from django.views.generic import  ListView
from django.views.generic.detail import  DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.
class Tasklistview(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'task'

class Taskdetailview(DetailView):
    model = task
    template_name = 'details.html'
    context_object_name = 'task1'

class Taskupdateview(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task2'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetails',kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')




def add(request):
    task2 = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')

        task1=task(name=name,priority=priority,date=date)
        task1.save()
    return render(request,'home.html',{'task':task2})

def delete(request,taskid):
    task1=task.objects.get(id=taskid)
    if request.method == 'POST':
         task1.delete()
         return redirect('/')

    return render(request,'delete.html')

def update(request,id):
    task1=task.objects.get(id=id)
    form1=TodoForm(request.POST or None,instance=task1)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form1,'task':task1})

# def details(request):
#     task1=task.objects.all()
#
#     return render(request,'details.html',{'task':task1})