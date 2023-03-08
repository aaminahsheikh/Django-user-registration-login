from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from . forms import CustomUserCreationForm

# Create your views here.


@login_required(login_url="login")
def home(request):
    context = {}

    return render(request, 'home/home.html', context)

def login_user(request):
    page = "login"
    context = {'page': page}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'home/login_user.html', context)

def logout_user(request):
    logout(request)

    return redirect("login")

def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # Pull that registered user
            user.save()

            user = authenticate(request, username=user.username,
                password=request.POST['password1'])

            if user:
                login(request, user)
                return redirect('home')

    context = {'form': form, 'page': page}
    return render(request, 'home/login_user.html', context)

