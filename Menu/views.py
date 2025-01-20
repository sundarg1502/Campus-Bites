from django.shortcuts import render,HttpResponse
from Menu.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, "menu.html",{"products":products})

def cart(request):
    return render(request,'cart.html')

def addtocart(request):
    print(request.GET.get("id"))
    return HttpResponse("Suucescc")