from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .models import Rider
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def index(request):
    return render(request,'index.html')
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

def LogoutPage(request):
    logout(request)
    return redirect('login')


def searchrider(request):
    if request.method == 'POST':
        pickup_location = request.POST.get('pickup')
        destination_location = request.POST.get('destination')

        if pickup_location and destination_location:
            riders = Rider.objects.filter(is_available=True)
            return render(request, 'searchresult.html', {'riders': riders})

    return render(request,'searchrider.html')
def detail(request, rider_id):
    rider = get_object_or_404(Rider, pk=rider_id)
    return render(request, 'riderdetail.html', {'rider': rider})