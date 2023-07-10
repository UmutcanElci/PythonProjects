from django.db import models
from django.utils import timezone
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
    
    
    
    