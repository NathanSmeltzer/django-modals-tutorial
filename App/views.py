from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Frontend
def frontend(request):
    return render(request, "frontend.html")

# Backend
@login_required(login_url="/login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def backend(request):
    return render(request, "backend.html")
# -----------------------------------------|

def Login(request):
    if request.user.is_authenticated:
        return render(request, "backend.html")
    else:
        messages.info(request, "Please log in")
        return HttpResponseRedirect("/")

def LoginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/backend")
        else:
            messages.info(request, "Username or password is incorrect")
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")

def LogoutUser(request):
    logout(request)
    request.user = None
    return HttpResponseRedirect("/")