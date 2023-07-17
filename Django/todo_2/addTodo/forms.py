from django.forms import ModelForm

from .models import *
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email'] # Form da Girilecek alanları oluşturur 
        

class AddToDoList(ModelForm):
    class Meta:
        model = ToDoList
        fields = ['task_title','task_category']