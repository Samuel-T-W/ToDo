from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo/addTodo/', views.addTodo, name='addTodo'),
    path('todo/deleteTodo/<int:todo_id>/', views.deleteTodo, name='deleteTodo'),
]