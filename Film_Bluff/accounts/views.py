from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # type: ignore
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, logout # type: ignore
from django.contrib import messages # type: ignore
from django.utils.safestring import mark_safe
from .models import Film
from .forms import SignUpForm, FilmForm
from django.http import HttpResponse



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
            user = form.save(commit=False)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            # Show a success popup and reset the form—no redirect
            messages.success(request, "🎉 Admin sign-up successful! Please log in below.")
            form = SignUpForm()
        else:
            # Collect form errors into a popup
            error_html = form.errors.as_ul()
            messages.error(
                request,
                mark_safe(f"🚨 Admin sign-up failed:<br>{error_html}")
            )
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

# accounts/views.py
@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    # handle form submission
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "🎬 Film added successfully!")
            return redirect('admin_dashboard')
        else:
            messages.error(request, "❌ Please fix the errors below.")
    else:
        form = FilmForm()

    movies = Film.objects.all()
    return render(request, 'accounts/admin_dashboard.html', {
        'movies': movies,
        'form':    form,
    })

@login_required
@user_passes_test(lambda u: u.is_staff)
def movie_add(request):
    # TODO: replace this stub with your real form/view logic
    return HttpResponse("🎬 Here will be your ‘Add a Film’ form.")


# User Logout
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

def home(request):
    return render(request, 'accounts/index.html')

@login_required
def account_overview(request):
    # Simple stub for now
    return render(request, 'accounts/account_overview.html')