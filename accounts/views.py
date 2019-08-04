from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username ALready Taken Dude')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.info(request,'Email ALready Taken Dude')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    print("user succsfully created")
                    return redirect('login')
     
        else:
            messages.info(request,'Watch Out For Password Dude')
            return redirect('register')


    else:
        return render(request,'accounts/register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            return redirect('dashboard')
        else:
            return redirect('register')
    else:
        return render(request,'accounts/login.html')
def logout(request):
    return redirect('index')
def dashboard(request):
    return render(request,'accounts/dashboard.html')

