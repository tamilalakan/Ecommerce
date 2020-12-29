from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from personal.forms import CreateUserForm, CreateUserAccount, CreateItem
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
# Create your views here.

from personal.models import Item, UserAccount, ThankYou

def home(request):
	if request.session.has_key('is_logged'):
		return render(request,"personal/home.html")
	else:
		return redirect('login')

def loginpage(request):
	if request.session.has_key('is_logged') is False:
		if request.method == "POST":
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				request.session['is_logged']=True
				return redirect('home')
			else:
				messages.info(request,"* Username or Password is incorrect")

		return render(request,"personal/login.html")
	else:
		return redirect('home')

def register(request):
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		form1 = CreateUserAccount(request.POST)
		if form.is_valid() and form1.is_valid():
			form.save()
			form1.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(request, username=username, password=raw_password)
			if user is not None:
				# login(request, user)
				return redirect('home')
	else:
		form = CreateUserForm()
	return render(request,"personal/register.html",{'form':form})

def logoutpage(request):
	logout(request)
	return redirect('home')



def product(request):
	context = {}
	l=[]
	prod = Item.objects.all()
	context['prod'] = prod
	for i in prod:
		if i.rate:
			s = float(i.rate)
			s = float(((25/100)*s))
			s = float(format(((float(i.rate) + s)), '.2f'))
			l.append(s)

	context['mrp'] = l
	return render(request, 'personal/product.html',context) 
 

def product_detail(request,id):
	context={}
	l, cartid=[], 0
	if id >= 369:
		id = abs(369 - id)
		cartid = id
	i = Item.objects.get(pk=id)
	
	if i.id == id:
		context['name'] = i.name
		context['image'] = i.main_image
		context['id'] = i.id + 369
		context['rate'] = i.rate
		context['short'] = i.short_des
		s = float(i.rate)
		s = float(((25/100)*s))
		s = float(format(((float(i.rate) + s)), '.2f'))
		l.append(s)
		context['mrp'] = l
		short = (i.description).split('.')
		short = short[0:len(short)-1]
		warrenty = (i.warrenty).split('.')
		warrenty = warrenty[0:len(warrenty)-1]
		context['warrenty'] = warrenty
		about = (i.about).split('.')
		about = about[0:len(about)-1]
		context['about'] = about
		context['description'] = short

		context['split'] = (i.name).split()

	if cartid > 0:
		b = UserAccount.objects.get(username=request.user)
		if b.productid is None:
			b.productid = " "
			b.save()
		b.productid += str(id) +' '
		b.save()

	return render (request,"personal/product_detail.html",context)

# Add Product
def addproduct(request):
	if request.method == 'POST':
		form = CreateItem(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	else:
		form = CreateItem()
	return render (request, "personal/addProduct.html",{"form":form})

# Cart Function
def cartfun(request):
	context,l,n = {}, [], []
	b = UserAccount.objects.get(username=request.user)
	sp = (b.productid).split(' ')
	sp = sp[1:len(sp)-1]
	for i in sp:
		
		cartitem = Item.objects.get(pk=i.strip())
		l.append(cartitem)
	
	s = set(l)
	for i in s:
		coun = l.count(i)
		n.append([i,coun])

	context['acc'] = n
	context['account'] = b
	return context

# Cart
def cart(request):
	useritem = UserAccount.objects.get(username=request.user)
	rm = (useritem.productid).split(' ')
	rm = (rm[1:len(rm)-1])
	strin = ' '
	error = ""
	if request.method == "POST":
		
		for i in rm:
			if request.POST.get(i) == 'decreament':
				rm.remove(i)
				break
			if request.POST.get(i) == 'increament':
				rm.append(i)
				print(rm.count(i))
				break
			if request.POST.get('type') == 'submit':
				form = CreateUserAccount(request.POST)
				if (useritem.firstname is None) and (form is not None):
					useritem.firstname = request.POST.get('firstname')
					useritem.lastname = request.POST.get('lastname')
					useritem.address = request.POST.get('address')
					useritem.city = request.POST.get('city')
					useritem.zipcode = request.POST.get('zipcode')
					useritem.state = request.POST.get('state')

					useritem.save()
					return redirect('buy')

				elif (useritem.firstname is not None):
					return redirect('buy')
				
				else:
					error = "*Kindly see and fill the address"


		for i in rm:			
			strin += str(i) + ' '
	
		useritem.productid = strin
		useritem.save()
		
	context = cartfun(request)
	context['total'] = total(rm)
	context['error'] = error

	return render(request,'personal/cart.html',context)

# Total Amount
def total(rm):
	total = 0
	sm = rm
	for i in set(sm):
		specific_item = Item.objects.get(pk=i)
		total += float(specific_item.rate)*(rm.count(i))
	total = round(total+50.98,2)
	return total


def remove(request,id):
	strin = " "
	rmv = UserAccount.objects.get(username=request.user)
	rm = (rmv.productid).split(' ')
	rm = (rm[1:len(rm)-1])

	for i in rm:
		if str(i) != str(id):
			strin += str(i) + ' '
	rmv.productid = strin
	rmv.save()

	context = cartfun(request)
	context['total'] = total(rm)
	return render(request,'personal/cart.html',context)
	

def buy(request):
	context = {}
	picture = ThankYou.objects.all()
	context['pic'] = picture
	# for i in picture:
	# 	print(i)
	return render(request,'personal/buy.html',context)