from django.contrib import messages
from django.http import response
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

# Create your views here.
def pg1(request):
     return redirect('main:chooseclass')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("login:pg1")
        else:
            messages.info(request,'invalid credentials')
            return redirect("login:login")
    else:
        return render(request, "login/login1.html",)

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
                return redirect('login:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('login:register')
            
            else:
                user = User.objects.create_user(username= username, password= password1, email=email, first_name= first_name,)
                user.save()
                print('user created')
                return redirect('login:login')
        else:
            messages.info(request,' password not matching..')
            return redirect('login:register')
        return redirect('/')
    else:       
        return render(request, "login/register1.html", )


def logout(request):
    auth.logout(request)
    return redirect('main:index')

