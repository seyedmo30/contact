from django.shortcuts import render,redirect,get_object_or_404
from .models import Phone
from .models import Grp
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
@login_required(login_url="signup")
def contacts(request,grp_id):
        group_id=get_object_or_404(Grp,pk=grp_id)
        groups=Grp.objects.all().filter(user=request.user)
        contacts=Phone.objects.all().filter(user=request.user).filter(group=group_id)
        return render(request,'phone/index.html',{'contacts':contacts,'groups':groups})

@login_required(login_url="signup")
def contacts_all(request):
        groups=Grp.objects.all().filter(user=request.user)
        contacts=Phone.objects.all().filter(user=request.user)
        return render(request,'phone/index.html',{'contacts':contacts,'groups':groups})


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

@login_required(login_url="signup")
def add(request):

    if request.method=='POST':
        grps=Grp.objects.all().filter(user=request.user)
        print(grps)

        if request.POST['name'] and request.POST['number'] and request.POST['group']  :
            phone=Phone()
            phone.name=request.POST['name']
            phone.number=request.POST['number']
            phone.group=request.POST ['group']
            phone.user=request.user
            phone.save()
            return redirect('/contacts/')
        else:

            groups=Grp.objects.all().filter(user=request.user)
            return render(request,'phone/add.html',{'error':'All field are required','groups':groups})

    else:
        groups=Grp.objects.all().filter(user=request.user)
        return render(request,'phone/add.html',{'groups':groups})


@login_required(login_url="signup")
def add_grp(request):

    if request.method=='POST':
        grps=Grp.objects.all().filter(user=request.user)
        print(grps)

        if request.POST['name'] and request.POST['number'] and request.POST['group']  :
            phone=Phone()
            phone.name=request.POST['name']
            phone.number=request.POST['number']
            phone.group=request.POST ['group']
            phone.user=request.user
            phone.save()
            return redirect('/contacts/')
        else:

            groups=Grp.objects.all().filter(user=request.user)
            return render(request,'phone/add.html',{'error':'All field are required','groups':groups})

    else:
        groups=Grp.objects.all().filter(user=request.user)
        return render(request,'phone/add.html',{'groups':groups})


def login (request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'] , password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('/contacts/')
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
