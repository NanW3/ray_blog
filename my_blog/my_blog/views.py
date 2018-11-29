from django.shortcuts import render, redirect, reverse
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import LoginForm, RegForm


def home(request):
    context = {}
    return render(request, 'home.html', context)

def login(request):
    print(request.user)
    print(request.environ)
    print (dir(request))
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
            login_form = LoginForm()

    context = {}
    context['login_form'] = login_form
    return render(request, 'login.html', context)

def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']

            user = User.objects.create_user(username, email, password)
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
            reg_form = RegForm()

    context = {}
    context['reg_form'] = reg_form
    return render(request, 'register.html', context)