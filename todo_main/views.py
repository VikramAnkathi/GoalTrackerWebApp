from django.shortcuts import render
from todo.models import Task

def home(Request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')

    dtasks = Task.objects.filter(is_completed=True)

    context = {
        'tasks': tasks,
        'dtasks': dtasks,
    }
    return render(Request, 'home.html',context)