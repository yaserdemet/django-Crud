from turtle import update
from django.shortcuts import render , redirect

# Create your views here.

from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm

def home(request):
    todos = Todo.objects.all()
    form = TodoForm()
    context = {
        "todos" : todos,
        "form" : form
    }
    return render (request , "todo/home.html" , context)


def todo_create(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    
    context = {
        "form" : form
    }
    return render (request , "todo/todo_add.html" , context)

# id delete ve update gereklidir
def todo_update(request , id):
    todo = Todo.objects.get(id=id)
    # !burada  update edilecek elemanı objetc.get(id=id) ile aldık
    form = TodoForm(instance=todo)
    # !burada ise bilgileri bir forma koyup göstermem gerek. bu yüzden TodoForm un içine attık
    
    if request.method == "POST":
        form = TodoForm(request.POST , instance=todo)
        if form.is_valid():
            form.save()
            return redirect("home")
    
    
    context = {
        "todo" : todo,
        "form"  : form
    }
    
    return render(request , "todo/todo_update.html" , context)


def todo_delete(request , id):
    todo = Todo.objects.get(id = id)
    if request.method == "POST":
        todo.delete()
        return redirect("home")
    
    context = {
        "todo" : todo
    }
    return render(request , "todo/todo_delete.html" , context)
    
