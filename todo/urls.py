from django.urls import path
from . import views


urlpatterns = [
    path("addTask/", views.addTask, name="addTask"),
    path("markasdone/<int:pk>", views.doneTask, name="doneTask"),
    path("markasundone/<int:pk>", views.undoneTask, name="undoneTask"),
    path("edit/<int:pk>", views.editTask, name="editTask"),
    path("delete/<int:pk>", views.deleteTask, name="deleteTask"),
]