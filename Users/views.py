from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import UserAccount, CustomUser
from django.contrib import messages



def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = CustomUser(
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone_number=form.cleaned_data['phone_number'],
            )
            user.set_password(form.cleaned_data['password'])
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

            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('dashboard')
        
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})



@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('login')