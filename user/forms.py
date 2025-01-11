from django import forms
from django.contrib.auth import get_user
from django.contrib.auth.forms import UserCreationForm

from .models import User

UserNew = get_user()


class CreatUser(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserNew
        fields = ('name', 'instagram', 'phone', 'adress')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'instagram', 'phone', 'adress']
