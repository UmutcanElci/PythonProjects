from django.forms import ModelForm

from .models import *
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email'] # Form da Girilecek alanları oluşturur 
        

    