from django import forms
from .models import CustomUser


class SignupForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    