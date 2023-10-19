from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import UserAccount, CustomUser
from django.contrib import messages
import random
from django.db.models.signals import post_save
from django.dispatch import receiver




def generate_unique_account_number():
    while True:
        account_number = ''.join(random.choice('0123456789') for _ in range(8))
        if not CustomUser.objects.filter(account_number=account_number).exists():
            return account_number


@receiver(post_save, sender=CustomUser)
def generate_user_account_number(sender, instance, created, **kwargs):
    if created:
        instance.account_number = generate_unique_account_number()
        instance.save()



def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = CustomUser(
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            user.set_password(form.cleaned_data['password1'])
            user.account_number = generate_unique_account_number()
            user.save()

            UserAccount.objects.create(user=user)
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid email or password')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})



@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('login')
