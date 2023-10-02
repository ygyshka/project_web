from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.shortcuts import render

# Create your views here.


class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserLogoutView(LogoutView):
    pass
