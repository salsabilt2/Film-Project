from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # type: ignore
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, logout # type: ignore
from django.contrib import messages # type: ignore
from .forms import SignUpForm


# User Registration
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            user.is_superuser = False
            user.save()
            messages.success(request, "🎉 Sign-up successful! Please log in below.")
            form = SignUpForm()  # reset form
        else:
            # collect all form errors into one string
            err = form.errors.as_ul()
            messages.error(request, mark_safe(f"🚨 Sign-up failed:<br>{err}"))
    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html', {'form': form})

def admin_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Grant admin privileges:
            user.is_staff = True
            user.is_superuser = True
            user.save()
            # Optionally log them in immediately:
            login(request, user)
            # After admin signup, send them to admin login (or dashboard)
            return redirect('admin_dashboard')
    else:
        form = SignUpForm()
    return render(request, 'accounts/admin_register.html', {'form': form})

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

def is_admin(user):
    return user.is_staff or user.is_superuser

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')


# User Logout
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

def home(request):
    return render(request, 'accounts/index.html')