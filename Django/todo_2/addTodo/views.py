from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from rest_framework.viewsets import ModelViewSet
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


def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Good")
    else:
        form = RegistrationForm()
        
    
    return render(request, 'addTodo/register.html',{"form":form})
            
        