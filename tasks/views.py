# tasks/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task  # Make sure you have a Task model defined
from .forms import TaskForm  # Make sure you have a TaskForm defined

def task_list(request):
    tasks = Task.objects.all()  # Get all tasks
    completed_tasks = [task for task in tasks if task.completed]
    uncomplete_tasks = [task for task in tasks if not task.completed]
    return render(request, 'tasks/task_list.html', {
        'completed_tasks': completed_tasks,  # Korrigierter Schlüssel
        'uncomplete_tasks': uncomplete_tasks  # Korrigierter Schlüssel
    })

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirect to task list after adding
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

def edit_task(request, pk):
    task = Task.objects.get(pk=pk)  # Get the task by primary key
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  # Update the existing task
            return redirect('task_list')  # Redirect to the task list
    else:
        form = TaskForm(instance=task)  # Pre-fill the form with the task's current data

    return render(request, 'tasks/edit_task.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')  # Redirect to task list after deleting
    return render(request, 'tasks/edit_task.html', {'task': task})

def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)  # Holt die Aufgabe anhand der ID
    if request.method == 'POST':
        task.completed = True  # Setzt das completed-Feld auf True
        task.save()  # Speichert die aktualisierte Aufgabe
        return redirect('task_list')  # Leitet zur Aufgabenliste weiter
    return redirect('task_list')  # Leitet auc

def uncomplete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)  # Holt die Aufgabe anhand der ID
    if request.method == 'POST':
        task.completed = False  # Setzt das completed-Feld auf True
        task.save()  # Speichert die aktualisierte Aufgabe
        return redirect('task_list')  # Leitet zur Aufgabenliste weiter
    return redirect('task_list')  # Leitet auc
