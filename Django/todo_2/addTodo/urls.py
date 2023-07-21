from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path("home",views.home,name="home"),
    path("register", views.register_user,name="register"),
    path("lists",views.seeList,name="lists"),
    path("addList",views.CreateTodoList.as_view(),name="addList"),
    path("addTask",views.CreateTodoTask.as_view(),name="addTask"),
    path("<str:todo_list_name>/tasks",views.seeTasks,name="tasks"),
    
    path("UpdateTodoList/<int:pk>",UpdateTodoList.as_view(),name="UpdateTodoList"),
    path("DeleteTodoList/<int:pk>/",DeleteTodoList.as_view(),name="DeleteTodoList"),
    
    path("UpdateTodoTask/<int:pk>/",UpdateTodoTask.as_view(),name="UpdateTodoTask"),
    path("DeleteTodoTask/<int:pk>/",DeleteTodoTask.as_view(),name="DeleteTodoTask"),
]
