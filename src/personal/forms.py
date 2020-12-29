from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserAccount, Item

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class CreateUserAccount(forms.ModelForm):
	class Meta:
		model = UserAccount
		fields = ['username','email','password1']

class CreateItem(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['name','short_des','description','warrenty','about','rate','image','main_image']

