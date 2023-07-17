from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from rest_framework.viewsets import ModelViewSet
from .models import *





# Create your views here.

def addList(request):
    queryset = ToDoList.objects.all()
    context = {'queryset': queryset}
    return render(request,'addTodo/lists.html',context)


def home(request):
    return render(request,'addTodo/home.html')

def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Good")
    else:
        form = RegistrationForm()
        
    
    return render(request, 'addTodo/register.html',{"form":form})
            
        