from django import forms
from .models import Resource

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['subjects'].choices = [('', '---------')]
    #     self.fields['courses'].choices = [('', '---------')]
    #     self.fields['form'].choices = [('', '---------')]
    #     self.fields['year'].choices = [('', '---------')]