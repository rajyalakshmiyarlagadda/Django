from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        def __init__(self, *args, **kwargs):
            super(UserRegisterForm, self).__init__(*args, **kwargs)
            self.fields['is_staff'].disabled = True
            self.fields['is_staff'].initial = 1

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

