from django.urls import path
from . import views 


urlpatterns = [
	path('register/',views.registerPage, name = 'register'),
	path('login/', views.loginPage, name = 'login'),
	path('', views.Home, name='home'),
	path('cards/', views.cardsPage, name = 'cards'),
	path('subsdaily/',views.subsdaily, name = 'subsdaily'),
	path('mystocks/',views.mystocksPage, name = 'mystocks')

]