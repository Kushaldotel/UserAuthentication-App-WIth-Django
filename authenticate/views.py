from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm

# Create your views here.
def home(request):
    return render(request, 'authenticate/home.html')

def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, ('You have been logged in Successfully'))
            return redirect('home')
            # return redirect('/login')
        else:
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html')
    
def logout_user(request):
    logout(request)
    messages.success(request,("You have been successfully logged out. You can login too."))
    return redirect('login')


def register_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request,user)
            messages.success(request, ('You have been Successfully registered:'))
            return redirect('home')

    else:
        form = SignupForm()

    context = {'form':form}
    return render(request, 'authenticate/register.html', context)