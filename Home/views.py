from django.shortcuts import render,redirect
from Home.forms import *
from django.contrib import messages
from django.contrib.auth import login as login_auth ,logout as logout_auth

# Create your views here.
def index(request):
    return render(request, "index.html")

def menu(request):
    return render(request, "menu.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def register(request):
    form = Register()
    if request.method == "POST":
        form = Register(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user_data = form.save(commit=False)
            user_data.set_password(form.cleaned_data["password"])
            form.save()
            messages.success(request,"Registration Successfull Please Login to continue")
            return redirect('Home:login')
        return render(request,"register.html",{"form":form})
    return render(request, "register.html")

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        # for error in form.errors:
        #     print(error)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login_auth(request,user)
                return redirect("Home:index")
            print("valid")
        return render(request, "login.html",{'form':form})
    return render(request, "login.html")

def logout(request):
    logout_auth(request)
    return redirect("Home:index")
