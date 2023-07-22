
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password'] 
    def init(self, args, **kwargs):
        super(RegistrationForm, self).init(args, **kwargs)
        
        

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))