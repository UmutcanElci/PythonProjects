from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages





# Create your views here.
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
            
        