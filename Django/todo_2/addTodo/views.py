from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.views.generic.edit import UpdateView,DeleteView
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

def addTodoList(request):
    if request.method == "POST":
        form = AddToDoList(request.POST)
        if form.is_valid():
            form.save()
            redirect("addTodo/home.html")
    else:
        form = AddToDoList()
    
    context = {"form": form}
    return render(request, 'addTodo/addList.html', context)

class UpdateTodoList(UpdateView):
    model = ToDoList
    fields = ['task_title','task_category']
    template_name = "addTodo/addList.html"
    success_url = reverse_lazy('lists')

class DeleteTodoList(DeleteView):
    model = ToDoList
    success_url = reverse_lazy('lists')
    template_name = 'addTodo/delete_confirmation.html'  

def addTodoTask(request):
    if request.method == "POST":
        form = AddToDoTask(request.POST)
        if form.is_valid():
            form.save()
            redirect("addTodo/home.html")
    else:
        form = AddToDoTask()
        
    context = {"form": form}
    return render(request,'addTodo/addTask.html',context)


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
            
        