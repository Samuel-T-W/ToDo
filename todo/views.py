from django.shortcuts import render, redirect

# Create your views here.

from .models import Todo
from .forms import TodoForm
from django.contrib.auth.models import User


def index(request):
	print(request.user)
	todo_data = Todo.objects.filter(user = request.user)
	form = TodoForm()
	content = {
		'todo_data': todo_data,
		'form' : form,
	}
	return render(request, 'todo/todo.html', content)

def addTodo(request):
	if request.method == 'POST':
		form = TodoForm(request.POST)
		if form.is_valid():
			print()
		print(form.errors)
		x = form.save(commit = False)
		x.user = request.user
		x.save()

	return redirect('index')


def deleteTodo(request, todo_id):
	Todo.objects.get(id = todo_id).delete()
	return redirect('index')
