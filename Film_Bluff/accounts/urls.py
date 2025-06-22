from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from accounts.views import home  # Import the homepage view


urlpatterns = [
        # Admin‐specific login — reuses the same login template, but will send you on to /admin/ afterward
    path('admin-login/',
         auth_views.LoginView.as_view(
             template_name='accounts/admin_login.html',
             redirect_authenticated_user=True
         ),
         name='admin_login'
    ),

    path(
           'admin-register/',
            views.admin_register,
            name='admin_register'
        ),

    path('register/', views.register, name='register'),  # Register page
    path('login/', auth_views.LoginView.as_view(
             template_name='accounts/login.html',
             redirect_authenticated_user=True),name='login'),  # Login page
    path(
            'admin-dashboard/',
            views.admin_dashboard,
            name='admin_dashboard'
        ),

    path('account/', views.account_overview, name='account_overview'),# User Account Overview

    path('logout/', views.logout_user, name='logout'),  # Logout functionality

    path('', views.home, name='home'),  # Home page
]