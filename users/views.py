from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserForm
from users.models import User


# Create your views here.


class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserLogoutView(LogoutView):
    pass


class UserRegisterView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        # new_user.is_active = False
        send_mail(
            subject='Поздровляем с регистрацией',
            message=f'Вы зарегистрировались на нашей платформе!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],

        )

        return super().form_valid(form)
