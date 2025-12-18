from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def home(request):
    todos = Todo.objects.all()
    return render(request, 'todoapp/index.html', {'todos': todos})

def add(request):
    if request.method == 'POST':
        Todo.objects.create(
            subject=request.POST['subject'],
            notes=request.POST['notes']
        )
        return redirect('home')
    return render(request, 'todoapp/form.html')

def edit(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.subject = request.POST['subject']
        todo.notes = request.POST['notes']
        todo.save()
        return redirect('home')
    return render(request, 'todoapp/form.html', {'todo': todo})

def view(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'todoapp/view.html', {'todo': todo})

def delete(request, id):
    Todo.objects.filter(id=id).delete()
    return redirect('home')
