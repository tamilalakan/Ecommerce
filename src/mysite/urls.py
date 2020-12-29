"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()

from personal.views import ( 
	home,
	loginpage,
	register,
	logoutpage,
	product,
	product_detail,
    addproduct,
    cart,
    remove,
    buy,
	)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name="home"),
    path('login', loginpage, name="login"),
    path('register', register, name="register"),
    path('logout', logoutpage, name="logout"),
    path('product', product, name="product"),
    path('product_detail/<int:id>', product_detail, name="product_detail"),
    path('addproduct', addproduct, name="addproduct"),
    path('cart', cart, name="cart"),
    path('cart/<int:id>', remove, name="remove"),
    path('buy', buy, name="buy"),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)