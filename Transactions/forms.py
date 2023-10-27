from django import forms
from .models import Subscription


class SubscriptionForm(forms.Form):
    phone_number = forms.CharField(max_length=10)

    class Meta:
        fields = ('phone_number',)