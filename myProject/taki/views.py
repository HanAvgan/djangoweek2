from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request,"about_us.html")
    
def cart(request):
    return render(request,"cart.html")   

def compair(request):
    return render(request,"compair.html")
    
def contact(request):
    return render(request,"contact.html") 

def forget_password(request):
    return render(request,"forget_password.html")

def fourcol(request):
    return render(request,"four-col.html") 

def general(request):
    return render(request,"general.html")   

def gridview(request):
    return render(request,"grid-view.html")   

def listview(request):
    return render(request,"list-view.html") 

def login(request):
    return render(request,"login.html")       

def product_details(request):
    return render(request,"product_details.html") 

def products(request):
    return render(request,"products.html") 

def register(request):
    return render(request,"register.html") 

def threecol(request):
    return render(request,"three-col.html")                
# Create your views here.
