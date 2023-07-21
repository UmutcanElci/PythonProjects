from django.forms import ModelForm

from .models import *
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email'] # Form da Girilecek alanları oluşturur 
    def init(self, args, **kwargs):
        super(RegistrationForm, self).init(args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'col-md-6'
        
