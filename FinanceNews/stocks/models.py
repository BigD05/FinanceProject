from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Stocknews(models.Model):
	users =models.ManyToManyField(User,blank=True)
	stock_name = models.CharField(max_length=100)
	stock_ticker = models.CharField(max_length=20)
	date = models.DateField(auto_now_add=True)
	stock_news = models.TextField(blank=True)

	def __str__(self):
		return self.stock_name
	
class Subtype(models.Model):
	users= models.OneToOneField(User, on_delete = models.CASCADE)
	daily_sub = models.BooleanField(default=False)
	weekly_sub = models.BooleanField(default=False)


