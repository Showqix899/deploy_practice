from django.shortcuts import render,redirect
from .models import Todo
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
    return render(request, 'home.html')


def register(request):

    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_todos')
    else:
        form=SignUpForm()
    return render(request,'register.html',{'form':form})

def login(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_todos')
        
        # Add authentication logic here
        return redirect('list_todos')




    return render(request,'login.html')


def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo = Todo(title=title, description=description)
        todo.save()
    return redirect('list_todos')


def complete_odo(request, todo_id):

    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('home')

def list_todos(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})

def home(request):
    return render(request, 'home.html')

def user_logout(request):
    logout(request)
    return redirect('login')


def todo_delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('list_todos')

def todo_complete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('list_todos')