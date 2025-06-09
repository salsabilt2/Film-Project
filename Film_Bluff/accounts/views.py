from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # type: ignore
from django.contrib.auth import login, logout # type: ignore
from django.contrib import messages # type: ignore
from .forms import SignUpForm


# User Registration
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)   # <— Use SignUpForm
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()   # <— And here
    return render(request, 'accounts/register.html', {'form': form})

# User Login
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}!')
            return redirect('home')  # Redirect to homepage after login
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# User Logout
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

def home(request):
    return render(request, 'accounts/index.html')