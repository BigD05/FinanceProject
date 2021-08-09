from django.db import models

# Create your models here.
#user model 
class User(models.Model):
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	date = models.DateField(auto_now_add=True)
	def __str__(self):
		return self.name
