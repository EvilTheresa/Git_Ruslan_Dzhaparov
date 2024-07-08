from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})


def detail_task(request, pk, **kwargs):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'detail_task.html', {'task': task})
def update_task(request, *args, pk, **kwargs):
    if request.method == "GET":
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(initial={
            "description": task.description,
            "due_date": task.due_date,
            "status": task.status,
        })
        return render(
            request, "update_task.html",
            context={"form": form}
        )
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = get_object_or_404(Task, pk=pk)
            task.description = request.POST.get("description")
            task.due_date = request.POST.get("due_date")
            task.status = request.POST.get("status")
            task.save()
            return redirect("task_list")
        else:
            return render(
                request,
                "update_task.html",
                {"form": form}
            )
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'delete_task.html', {'task': task})