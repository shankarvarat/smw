from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.forms import UserCreationForm

m="male"
f="female"
gen=[(m,'m'),(f,'f')]
s="Singale"
M="Married"
rel=[(s,'s'),(M,'M')]

class profile(models.Model):
    user=models.OneToOneField(User,on_delete='CASCADE')
    nickname=models.CharField(max_length=50)
    dob=models.DateField(null=True)
    phoneno=models.IntegerField()
    gender=models.CharField(choices=gen,max_length=50)
    relation=models.CharField(choices=rel,max_length=50)

class frends(models.Model):
        user = models.OneToOneField(User, on_delete='CASCADE')
        frend= models.CharField(max_length=50)
        status = models.BooleanField(default=False)
class post(models.Model):
    post_d=models.TextField(max_length=300)
    created_at=models.DateField(auto_now_add=True)
    tag=models.ForeignKey(frends,null=True,on_delete='CASCADE')
    user=models.OneToOneField(User,on_delete='CASCADE')
