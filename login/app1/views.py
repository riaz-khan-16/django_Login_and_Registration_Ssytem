from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

# Create your views here.



def  registration(request):

    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']

        my_user=User.objects.create_user(username,email,password)
        my_user.first_name=fname
        my_user.last_name=lname
        my_user.save()
        return redirect('login1')

        

    return render(request,"registration.html")

def  login1(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)

        if user is not  None:
              login(request,user)
              return render(request,'home.html',{'fname': username})
        
        else:
            print('credential is wrong')







    return render(request,"login.html")

def  logout1(request):
    logout(request)
    return render(request,"login.html")

@login_required
def  home(request):
    return render(request,"home.html")

@login_required(login_url="/")
def home2(request):

    return render(request,"home2.html")


