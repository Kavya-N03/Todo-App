from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


# User Registeration
def registerUser(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully!')
            return redirect('login')
        else:
            messages.error(request, 'An error occurred during registration')
    else:
        form = UserCreationForm()
    return render(request, 'todo/register.html', {"form": form})


# User Login
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username').strip()
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Username or Password")
    return render(request, 'todo/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

#Home Page
@login_required(login_url='login')
def home(request):
    tasks = Task.objects.filter(user=request.user)
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request,'Task created successfully!')
            return redirect('home')
    context = {"form": form, "tasks": tasks}
    return render(request, 'todo/home.html', context)

#Edit task
def task_Update(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,'Task updated successfully!')
            return redirect('home')
    return render(request, 'todo/home.html', {"form": form})

# Delete task
def task_Delete(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request,'Task deleted successfully!')
        return redirect('home')
    return render(request, 'todo/delete.html', {"tasks": task})
