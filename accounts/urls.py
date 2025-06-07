from django.urls import path
from . import views
from django.contrib import admin
from accounts.views import home  # Import the homepage view


urlpatterns = [
    path('register/', views.register, name='register'),  # Register page
    path('login/', views.login_user, name='login'),  # Login page
    path('logout/', views.logout_user, name='logout'),  # Logout functionality
    path('', views.home, name='home'),  # Home page
]