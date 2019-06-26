from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def signup(request):
    signupform=UserCreationForm
    if request.method == "POST":
        signupform=UserCreationForm(request.POST)
        if signupform.is_valid():
            signupform.save()
            redirect('login')
        else :
            error="Please fill correctaly !!"
            return render(request, 'signup.html', {'signupform': signupform,'error':error})
    else :

        return render(request,'signup.html',{'signupform':signupform})
def home(request):
    form=profileform()
    return render(request,'index.html',{'form':form})




