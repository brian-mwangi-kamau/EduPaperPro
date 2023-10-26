from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Transaction
from Users.models import CustomUser
from django_daraja.mpesa.core import MpesaClient

