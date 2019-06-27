from django import forms
from django.contrib.auth.models import User
from .models import *



class profileform(forms.ModelForm):
    class Meta:
         model=profile
         fields='__all__'
class postform(forms.ModelForm):
     class Meta:
         model=post
         fields=('post_d','user')


