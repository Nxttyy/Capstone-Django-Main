from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm, LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from bookApp.models import Book


# Create your views here.
def register(request):
	if request.method == "POST":
		form = CustomUserCreationForm(request.POST, request.FILES)
		if form.is_valid():
			# print(request.FILES)
			form.save()
			messages.success(request, "Account Created")
			return redirect("login")
			
	else:
		form = CustomUserCreationForm()
	return render(request, 'users/registration.html', {'form':form})

def login(request):
	if request.method == "POST":
		form = LoginUserForm(request, data=request.POST)
		if form.is_valid():
			print("%%")
			email = request.POST.get("username")
			print(request.POST)
			# email = 'nus@gmail.com'
			password = request.POST.get("password")
			# password = 'asdf1234!@#$'
			user = authenticate(request, username = email, password = password)

			if user is not None:
				auth.login(request,user)
				return redirect("book-home")
	else:
		form = LoginUserForm()

	context = {"form": form}
	return render(request, "users/login.html", context)


def log_out(request):
    auth.logout(request)
    return redirect("book-home")

@login_required
def account(request):
	# context = {"form": form}
	user = request.user
	# print(user.first_name)

	context = {"user": user, "borrowed_books":user.book_set.all() }
	print(user.book_set.all())
	for b in user.book_set.all():
		print("*")
		print(b.title)
		print(b.borrowers)

	print()
	
	return render(request, "users/account.html", context)
