from django.shortcuts import render,redirect
from .forms import CreateUserForm, LoginUserForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def registration(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            current_user = form.save(commit=False)
            form.save()
            send_mail("Welcome to kunthought!", "Congratulations on creating your account", settings.DEFAULT_FROM_EMAIL, [current_user.email])
            messages.success(request, "Account Created")
            return redirect("login")
    context = {"registration_form": form}
    return render(request,"registration.html", context)

def log_in(request):
    form = LoginUserForm()
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username = username, password = password)
            if user is not None:
                auth.login(request,user)
                return redirect("/")
    context = {"login_form": form}
    return render(request, "login.html", context)

def log_out(request):
    auth.logout(request)
    return redirect("homepage")