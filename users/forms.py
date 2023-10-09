from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
# UserCreationForm, AuthenticationForm, BaseUserCreationForm
from django.core.exceptions import ValidationError

from catalog.forms import MixinForm
from users.models import User
from users.utils import send_email_for_verify


class ProfileUserForm(MixinForm, UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone', 'country', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class UserForm(MixinForm, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password')


class MyAuthenticationForm(MixinForm, AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get("username")
        # username = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )

            # if self.user_cache is None:
            #     raise ValidationError(
            #         self.error_messages["invalid_login"], #- В базовом классе django в сообщении граматическая ошибка!?
            #         code="invalid_login",
            #         params={"username": self.username_field.verbose_name},
            #     )

            # if self.user_cache is None:
            #     raise ValidationError(
            #         'Пожалуйста, введите правильные логин и пароль. Оба поля могут быть чувствительны к регистру.',
            #         # self.error_messages["invalid_login"],
            #         code='invalid_login',
            #     )

            if self.user_cache is None:
                raise self.get_invalid_login_error()

            elif not self.user_cache.email_verify:
                send_email_for_verify(self.request, self.user_cache)
                raise ValidationError(
                    'Почта не верифицирована, проверьте вашу почту!',
                    code='invalid_login',
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data



