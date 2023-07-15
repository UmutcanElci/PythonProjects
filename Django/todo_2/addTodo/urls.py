from django.urls import path
from . import views

urlpatterns = [
    path("register.html", views.register_user,name="register"),
]
