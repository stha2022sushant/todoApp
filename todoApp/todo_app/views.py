
from django.shortcuts import render, redirect
from .models import Task

# Display all tasks
def home(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'todo_app/home.html', {'tasks': tasks})

# Add a new task
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
    return redirect('home')

# Mark a task as completed/uncompleted
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('home')

# Delete a task
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')
