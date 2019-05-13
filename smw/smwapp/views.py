from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Author
from .forms import *

# Create your views here.
def home(request):

    data=Post.objects.all()
    return render(request,"index.html",{'data':data})

def authorform(request):
    form=AuthorForm()
    if request.method=='POST':
        form=AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'authorform.html',{'form':form})
        else:

            return render(request,'authorform.html',{'form':form})
    else:
        return render(request, 'authorform.html', {'form': form})
def postform(request):
    form=Postform()
    if request.method=='POST':
        form=Postform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'postform.html',{'form':form})
        else:

            return render(request,'postform.html',{'form':form})
    else:
        return render(request, 'postform.html', {'form': form})

