from django.shortcuts import render, redirect
from django.http import Http404
from .models import Todo

from .forms import TaskForm
# Create your views here.


def todo(request):
    todos = Todo.objects.all()
    context = {"todos": todos}
    return render(request, 'todostuff/index.html', context)


def delete(request, task_id):
    # Get the product based on its id
    todo = Todo.objects.get(id=task_id)

    # if this is a POST request, we need to delete the form data
    if request.method == 'POST':
        todo.delete()
        # after deleting redirect to view_product page
        return redirect('index')

    # if the request is not post, render the page with the product's info
    return render(request, 'todostuff/delete.html', {'todo': todo})


def complete(request, task_id):
    todo = Todo.objects.get(id=task_id)

    # if this is a POST request, we need to delete the form data
    if request.method == 'POST':
        todo.completed = True
        todo.save()
        # after deleting redirect to view_product page
        return redirect('index')

    raise Http404()


def update_post(request, task_id):
    post = Todo.objects.get(id=task_id)
    form = TaskForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'todostuff/update.html', {'form': form})


def add_todo(request):
    if request.method == "POST":
        todo_text = request.POST.get("todo_text", None)
        if todo_text:
            Todo.objects.create(text=todo_text)
            return redirect('index')
    else:
        raise Http404()
