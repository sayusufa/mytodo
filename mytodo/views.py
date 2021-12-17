from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, UpdateForm
from django.contrib import messages

def home(request):
    tasks = Task.objects.all().order_by('Date', 'time_todo')
    num = tasks.count()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('Task added successfully!'))
            return redirect('home_page')

    tasks = Task.objects.all().order_by('Date', 'time_todo')
    return render(request,'mytodo/home.html', {'tasks': tasks, 'form': form, 'num': num})

def executed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_executed = True
    task.save()
    return redirect('home_page')


def unexecuted(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_executed = False
    task.save()
    return redirect('home_page')

def edit(request, task_id):
    task = Task.objects.get(id=task_id)
    form = UpdateForm(instance=task)
    if request.method == 'POST':
        form = UpdateForm(request.POST or None, instance=task)

        if form.is_valid():
            form.save()
            messages.success(request, ('Task has been edited!'))
            return redirect('home_page')

    
    return render(request, 'mytodo/edit.html', {'form': form})

def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    messages.success(request, ('Task deleted!'))
    return redirect('home_page')

def warn_user_deleting_all(request):
    tasks = Task.objects.all()
    if tasks:
        return render(request, 'mytodo/clear_tasks.html')
    return redirect('home_page')

def delete_all(request):
    tasks = Task.objects.all()
    tasks.delete()
    messages.success(request, ('Tasks deleted all!'))
    return redirect('home_page')