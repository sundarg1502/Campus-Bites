from django.shortcuts import render
from django.http import JsonResponse
from Menu.models import Product,Cart
import json

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, "menu.html",{"products":products})

def cart(request):
    print(request.user)
    cart = Cart.objects.filter(user=request.user.id)
    total = 0
    count= 0
    for data in cart:
        count+=1
        total+=data.product.discount_price*data.quantity
    print(total)
    return render(request,'cart.html',{"items":cart,"total":total,"count":count})

def addtocart(request):
    if request.user.is_authenticated:
        data = json.load(request)
        pid = Product.objects.get(pk=data['id'])
        Cart.objects.create(product=pid,user=request.user,quantity=data['qty'],amount=data["amount"])
        return JsonResponse({"Ststus":'Successs'},status=200)
    else:
        return JsonResponse({"status":"User Login Required"},status=200)