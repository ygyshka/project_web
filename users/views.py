from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.contrib.auth.tokens import (default_token_generator
                                        as token_generator)
from django.views.generic import CreateView, UpdateView

from users.forms import MyAuthenticationForm, UserForm, ProfileUserForm
from users.models import User
from users.utils import send_email_for_verify


# Create your views here.


class UserLoginView(LoginView):
    form_class = MyAuthenticationForm
    template_name = 'users/login.html'


class UserLogoutView(LogoutView):
    pass


class Register(View):

    template_name = 'users/register.html'

    def get(self, request):
        context = {
            'form': UserForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            send_email_for_verify(request, user)
            return redirect('users:confirm_email')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class EmailVerify(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('catalog:home')

        return redirect('users:invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            User.DoesNotExist,
            ValidationError,
        ):
            user = None
        return user

class ProfileUpdateView(UpdateView):

    model = User
    form_class = ProfileUserForm
    # success_url = redirect('users:profile')
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):



        return self.request.user
