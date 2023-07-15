from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
class ToDoList(models.Model):
      TASK_CODES = [
        ("JB","Job"),
        ("DL","Daily"),
        ("HB","Habit"),
        ("ED","Education"),
        ("HL","Holiday"),
    ]
      task_title = models.CharField(max_length=60)
      task_category = models.CharField(max_length=2,choices=TASK_CODES)
      
      def __str__(self) -> str:
           return self.task_title
    


class ToDoTask(models.Model):
    task_name = models.CharField(max_length=60)
    task_description = models.TextField(null=True,blank=True)
    task_complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    todo_list = models.ForeignKey(ToDoList,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
         return self.task_name
    

class User(AbstractBaseUser):
  username = models.CharField(max_length=50,unique=True)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=100)
  phone = models.IntegerField(null=True,unique=True)
  address = models.CharField(max_length=150,null=True)
  
  
  USERNAME_FIELD = "username"
  REQUIRED_FIELDS = ["email"]
  
   
  
    
    