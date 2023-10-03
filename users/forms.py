from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from catalog.forms import MixinForm
from users.models import User
from users.utils import send_email_for_verify


class UserForm(MixinForm, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class MyAuthenticationForm(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if not self.user_cache.email_verify:
                send_email_for_verify(self.request, self.user_cache)
                raise ValidationError(
                    'Почта не верифицирована, проверьте вашу почту!',
                    code='invalid_login',
                )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

