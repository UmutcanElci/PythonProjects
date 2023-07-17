from django.urls import path
from . import views
from django.conf.urls import static

urlpatterns = [
    path("home",views.home,name="home"),
    path("register", views.register_user,name="register"),
    path("lists",views.addList,name="lists")
]
