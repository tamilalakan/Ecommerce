from django.db import models

# Create your models here.

class Item(models.Model):
	name 		= models.CharField(max_length=32)
	short_des 	= models.TextField(null=True)
	description = models.TextField()
	warrenty 	= models.TextField(null=True)
	about 		= models.TextField(null=True)
	rate 		= models.FloatField(max_length=32, null=True)
	image 		= models.ImageField(blank=True, null=True)
	main_image 	= models.ImageField(blank=True, null=True)	

	def __str__(self):
		return self.name

class UserAccount(models.Model):
	username 	= models.CharField(max_length=32)
	email 		= models.EmailField(null=True)
	password1 	= models.CharField(max_length=42)
	productid 	= models.CharField(max_length=53, blank=True, null=True)
	firstname 	= models.CharField(max_length=32, blank=True, null=True)
	lastname 	= models.CharField(max_length=32, blank=True, null=True)
	address 	= models.TextField(max_length=100, blank=True, null=True)
	city 		= models.CharField(max_length=32, blank=True, null=True)
	zipcode		= models.CharField(max_length=32, blank=True, null=True)
	state 		= models.CharField(max_length=32, blank=True, null=True)


	def __str__(self):
		return self.username

class ThankYou(models.Model):
	name		= models.CharField(max_length=32, blank=True, null=True)
	picture 	= models.ImageField(upload_to='upload')

	def __str__(self):
		return self.name