from typing import Set
from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse,reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth.hashers import make_password


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
     

    

#@login_required(login_url="/login")
def seeTasks(request, todo_list_name):
    todo_list = ToDoList.objects.get(task_title=todo_list_name)
    queryset = ToDoTask.objects.filter(todo_list=todo_list)
    context = {'queryset': queryset}
    return render(request, 'addTodo/tasks.html', context)

    

class RegisterUser(CreateView):
    form_class = RegistrationForm
    template_name = "addTodo/register.html"

    def form_valid(self, form):
        
        form.instance.password = make_password(form.cleaned_data['password'])
        
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("login")


class LoginUser(LoginView):
    template_name="addTodo/login.html"
    redirect_authenticated_user = True
    def get_success_url(self) -> str:
        print("Good")
        return reverse_lazy('lists')
    
    def form_invalid(self, form):
     print(form.errors)
     messages.error(self.request, "Invalid username or password")
     return self.render_to_response(self.get_context_data(form=form))
    
    
class LogoutUser(LogoutView):
    template_name = "addTodo/logout_confirm.html"
    redirect_field_name = "login"
    print("Logout")
    reverse_lazy("login")