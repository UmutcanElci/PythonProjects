from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("home",views.home,name="home"),
    path("register", views.register_user,name="register"),
    path("lists",views.seeList,name="lists"),
    path("addList",views.addTodoList,name="addList"),
]
