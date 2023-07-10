from django.urls import path

urlpatterns = [
    path("",name="index"),
    path("<str:task_title>/",name="list"),
    path("<str:task_title>/<str:task_name>/",name="task")
]
