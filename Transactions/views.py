from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Transaction
from Users.models import CustomUser
from django_daraja.mpesa.core import MpesaClient
from .forms import SubscriptionForm
from django.views.decorators.csrf import csrf_exempt
import json



stk_push_callback_url = 'https://edupaperpro.pythonanywhere.com/success'

@login_required
def subscription_page(request):
    return render(request, 'subscription_page.html')



# STK push for 200 shillings for one month subscriptions
# This specific view is working fine. To test is, head to http://127.0.0.1:8000/payments/api/sub/ and input a valid Safaricom phone number.
@login_required
def subscription_initiation_monthly(request):
    user = request.user
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            cl = MpesaClient()
            phone_number = form.cleaned_data['phone_number']
            amount = 200
            account_reference = user.account_number
            transaction_desc = 'One Month subscription'
            callback_url = stk_push_callback_url
            response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
            return HttpResponse("Subscription initiation successful. You will receive a payment request shortly.")
        
    else:
        form = SubscriptionForm()
    return render(request, 'subscription_page', {'form': form})


# STK push for 2000 shillings for one year subscriptions
@login_required
def subscription_initiation_yearly(request):
    user = request.user
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            cl = MpesaClient()
            phone_number = form.cleaned_data['phone_number']
            amount = 2000
            account_reference = user.account_number
            transaction_desc = 'One year subscription'
            callback_url = stk_push_callback_url
            response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
            return HttpResponse("Subscription initiation successful. You will receive a payment request shortly.")
        
    else:
        form = SubscriptionForm()
    return render(request, 'subscription_page', {'form': form})