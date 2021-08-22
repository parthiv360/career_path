from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

# Create your views here.
def pg1(request):
     return render(request,'login/pg1.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("pg1")
        else:
            messages.info(request,'invalid credentials')
            return redirect("login")
    else:
        return render(request, "login/login.html",)

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        
        username = request.POST['username']
            
        email = request.POST['email']
        password1 = request.POST['password1']

        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            
            else:
                user = User.objects.create_user(username= username, password= password1, email=email, first_name= first_name,)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request,' password not matching..')
            return redirect('register')
        return redirect('/')
    else:       
        return render(request, "login/register.html", )