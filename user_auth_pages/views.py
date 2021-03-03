from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import CreateUserForm

def register(request):
	if request.method == "POST":
		form = CreateUserForm(data=request.POST)

		if form.is_valid():
			form.save()
			return redirect('display_task_lists')

	else:
		form = CreateUserForm()

	return render(request, 'pages/register.html', {'form' : form})

def dashboard(request):
	return render(request, 'pages/dashboard.html')

def user_login(request):
	if request.user.is_authenticated:
		return redirect('dashboard')

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('dashboard')
		
		else:
			messages.error(request, 'Username or password is incorrect')

	return render(request, 'pages/login.html')

def user_logout(request):
	if request.user.is_authenticated:
		logout(request)

	return redirect('login')