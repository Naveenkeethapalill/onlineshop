from django.shortcuts import render ,  redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from . models import Product
from cart.cart import Cart

@login_required
def index(request):
    product=Product.objects.all()
    return render (request,'index.html',{'product':product})
def signin (request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render (request, 'signin.html',{'form':form})
def login(request):
    return render (request,'login.html')
def cart(request):
    return render (request,'cart.html')

@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")

@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("index")

def readmore(request,id):
    product = Product.objects.get(id=id)
    return render (request,'readmore.html',{'product':product})

   

