from django.contrib.auth.forms import UserCreationForm

from catalog.forms import MixinForm
from users.models import User


class UserForm(MixinForm, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
