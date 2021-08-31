from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Stocknews,Subtype
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def mystocksPage(request):
	user_info = Subtype.objects.get(user=request.user)
	user_stocks = user_info.stock_ticker.all()
	context = {'user_stocks': user_stocks}
	if request.method == 'POST':
		data = request.POST['stock_name']
		stock_news = Stocknews.objects.get(stock_name=data)
		user_info.stock_ticker.remove(stock_news)

	return render(request,'stocks/mystocks.html',context)

def subsdaily(request):
	subtype = Subtype.objects.filter(user=request.user)

	context = {'user': request.user,}
	if request.method == 'POST':
		is_daily = request.POST.get('daily_sub', 'off')
		is_weekly = request.POST.get('weekly_sub', 'off')
		return redirect('cards')
		if is_daily == 'on':
			subtype.update(daily_sub = True)
			subtype.update(weekly_sub = False)
		elif is_weekly == 'on':
			subtype.update(weekly_sub = True)
			subtype.update(daily_sub = False)
			return redirect('cards')
		
	return render(request,'stocks/subsdaily.html')

def cardsPage(request):
	data = Stocknews.objects.all()
	context = {'data': data}

	if  request.method == 'POST':
		subtype = Subtype.objects.get(user=request.user)
		data = request.POST['stock_name']
		stock_news = Stocknews.objects.get(stock_name=data)
		subtype.stock_ticker.add(stock_news)
		return redirect('subsdaily')
	return render(request, 'stocks/cards.html',context)

def Home(request):
	return render(request, 'stocks/home.html')


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
			subtype = Subtype.objects.get_or_create(user = request.user)
			if subtype == True:
				return redirect('home')
			else:
				return redirect('home')
			
		else:
			messages.info(request,'Username or Password is inccorect')
				
	context = {}
	return render(request, 'stocks/login.html')


def logoutUser(request):
	logout(request)
	return redirect('login')

