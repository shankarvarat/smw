from django import forms

from .models import *

class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields='__all__'
class Postform(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'