from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.urls import reverse,reverse_lazy
from .models import *

from .forms import *



# Create your views here.
def home(request):
    return render(request,'addTodo/home.html')

def seeList(request):
    queryset = ToDoList.objects.all()
    context = {'queryset': queryset}
    return render(request,'addTodo/lists.html',context)

class CreateTodoList(CreateView):
    model = ToDoList
    fields = ['task_title', 'task_category']
    template_name = 'addTodo/addList.html'
    success_url = reverse_lazy('lists')

    def form_valid(self, form):
        task_title = form.cleaned_data['task_title']
        
        if ToDoList.objects.filter(task_title=task_title).exists():
            form.add_error('task_title', 'A list with this title already exists.')
            return self.form_invalid(form)
    
        return super().form_valid(form)
    
    
class UpdateTodoList(UpdateView):
    model = ToDoList
    fields = ['task_title','task_category']
    template_name = 'addTodo/update_confirmation.html'
    success_url = reverse_lazy('lists')
    
    def form_valid(self, form):
        task_title = form.cleaned_data['task_title']
        
        if ToDoList.objects.filter(task_title=task_title).exists():
            form.add_error('task_title', 'A list with this title already exists.')
            return self.form_invalid(form)
    
        return super().form_valid(form)
    

class DeleteTodoList(DeleteView):
    model = ToDoList
    success_url = reverse_lazy('lists')
    template_name = 'addTodo/delete_confirmation.html'  

class CreateTodoTask(CreateView):
    model = ToDoTask
    fields = ['task_name','task_description','todo_list']
    template_name = "addTodo/addTask.html"
    def get_success_url(self) -> str:
        todo_list_name = self.object.todo_list.task_title
        return reverse('tasks', kwargs={'todo_list_name':todo_list_name})


class UpdateTodoTask(UpdateView):
    model = ToDoTask
    fields = ['task_name', 'task_description', 'todo_list']
    template_name = "addTodo/addTask.html"
    
    def get_success_url(self) -> str:
        todo_list_name = self.object.todo_list.task_title
        return reverse('tasks', kwargs={'todo_list_name':todo_list_name})



class DeleteTodoTask(DeleteView):
    model = ToDoTask
    success_url = reverse_lazy('lists')
    template_name = 'addTodo/delete_confirmation.html' 
     

    


def seeTasks(request, todo_list_name):
    todo_list = ToDoList.objects.get(task_title=todo_list_name)
    queryset = ToDoTask.objects.filter(todo_list=todo_list)
    context = {'queryset': queryset}
    return render(request, 'addTodo/tasks.html', context)

    

def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Good")
    else:
        form = RegistrationForm()
        
    
    return render(request, 'addTodo/register.html',{"form":form})
            
        