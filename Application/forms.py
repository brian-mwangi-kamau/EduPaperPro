from django import forms
from .models import Resource
from Users.models import CustomUser


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'


class UpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
        )