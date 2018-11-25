from django.shortcuts import render, redirect
from django.contrib import auth


def home(request):
    context = {}
    return render(request, 'home.html', context)

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(request, username=username, password=password)
    referer = request.META.get('HTTP_REFERER', '/')
    if user is not None:
        auth.login(request, user)
        return redirect(referer)
    else:
        return render(request, 'error.html', {'message': 'Username/Password incorrect!'})