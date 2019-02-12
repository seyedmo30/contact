from django.shortcuts import render,redirect
from .models import Phone
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login")
def contacts(request):
    contacts=Phone.objects.all().filter(user=request.user)
    return render(request,'phone/index.html',{'contacts':contacts})

def signup(request):
    if request.method=='POST':
        if request.POST['password']==request.POST['confirm']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'phone/signup.html',{'error':'user alredy'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password'])
                auth.login(request,user)
                return redirect('signup')
        else:
            return render(request,'phone/signup.html',{'error':'password must be match'})



    else:
        return render(request,'phone/signup.html')


def login (request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'] , password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('contacts')
        else:
            return render(request,'phone/login.html',{'error':'username or password is incorrect'})
    else:
        return render(request,'phone/login.html')



def logout (request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')

    else:
        return render(request,'phone/login.html')
