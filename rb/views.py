from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Username or Password is incorrect')


    return render(request, template_name='login.html')
def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('password')


        user= User.objects.create_user (username=username, email=email, password=password)
        user= authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request,user)
            messages.success(request,'you have successfully sign up')
            return redirect('login')

    return render(request, template_name='signup.html')
