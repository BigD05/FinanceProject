from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from .models import Stocknews
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def Home(request):
	data = Stocknews.objects.all()
	context={
	'data': data
	}
	return render(request, 'stocks/home.html',context)


def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request,'Your Account was created successfully! ' + user)
			return redirect('login')
	context = {'form':form}
	return render(request, 'stocks/register.html',context)



def loginPage(request):
	if request.method =='POST':
		username =request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request,username = username, password = password)
		if user is not None:
			login(request,user)
			return redirect('home')
		else:
			messages.info(request,'Username or Password is inccorect')
				
	context = {}
	return render(request, 'stocks/login.html')


def logoutUser(request):
	logout(request)
	return redirect('login')

