from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Transaction
from Users.models import CustomUser
from django_daraja.mpesa.core import MpesaClient
from .forms import SubscriptionForm
from django.views.decorators.csrf import csrf_exempt
import _json


'''
What I am trying to do here is collect the user's phone number from them, and initiate a push to pay 200kes to the system
for a monthly subscription.
Transactions will be identified and linked to users using an 8-digit account number that every user has.(unique)
After a successful transaction, a field named "is_subscribed" in Users.CustomUser will be set to "True" which will now allow
the specific user to access all the materials on the platform.
I'll use Celery to handle the logic for setting the "is_subscribed" field back to False when 31 days are gone after a successful transaction(subscription)
'''


# STK push for 200 shillings for one month subscriptions
# This specific view is working fine. To test is, head to http://127.0.0.1:8000/payments/api/sub/ and input a valid Safaricom phone number.
@login_required
def subscription_initiation(request):
    user = request.user
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            cl = MpesaClient()
            phone_number = form.cleaned_data['phone_number']
            amount = 200
            account_reference = user.account_number
            transaction_desc = 'One Month subscription'
            callback_url = 'https://api.darajambili.com/express-payment'
            response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
            return HttpResponse("Subscription initiation successful. You will receive a payment request shortly.")
        
    else:
        form = SubscriptionForm()
    return render(request, 'subscription_form.html', {'form': form})



# The view below should be the view whose url endpoints will be used as the callback url.

# @csrf_exempt
# def express_payment_callback(request):
#     if request.method == 'POST':



