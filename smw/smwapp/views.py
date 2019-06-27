from django.shortcuts import render,redirect
from .models import post,frends,profile
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate
# Create your views here.
from django.contrib.auth.models import User


@login_required
def spe(request):
    return HttpResponse("You are logged in !")
def login(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('/home')
                else:
                    return HttpResponse("Your account was inactive.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username, password))
                return HttpResponse("Invalid login details given")
        else:
            return render(request, 'login.html', {})


        
def signup(request):
    signupform=UserCreationForm
    if request.method == "POST":
        signupform=UserCreationForm(request.POST)
        if signupform.is_valid():
            signupform.save()

            return redirect('home')
        else :
            error="Please fill correctaly !!"
            return render(request, 'signup.html', {'signupform': signupform,'error':error})
    else :

        return render(request,'signup.html',{'signupform':signupform})
def home(request):
     #name=user
    form=profileform()

    data1=User.objects.all()

    #="Not Found"
    data2=frends.objects.all() #p1.objects.all()  #post.objects.all()
    data3="post data not found"  #post.objects.all()
    return render(request,'index.html',{'form':form,'data1':data1,'data2':data2,'data3':data3})

def profile(request):
    form=profileform()
    if request.method == 'POST':
        form=profileform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'index.html')
        else:
            error="Some Errors are find !! Plese fill correctaly !!"
            return render(request,'profile.html',{"form":form,'error':error})
    else:
        return render(request,'profile.html',{'form':form})



@login_required()
def post(request):
    #form=postform(initial={'username':request.user.username})
    form = postform()

    if request.method=='POST':

        form=postform(request.POST)
        if form.is_valid():
            form.save()
            '''username=request.
            
            form = postform(request.POST,initial=username)
            instance = form.save(commit=False)
            instance.username = request.user
            instance.save()'''

            #form.save()
            return render(request,'index.html')
        else:
            error="Plese Fill Form Correctaly"
            return render(request,'post.html',{'form':form,'error':error})
    else:
        return render(request, 'post.html', {'form': form})

