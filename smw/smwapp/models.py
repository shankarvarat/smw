from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.forms import UserCreationForm

m="m"
f="f"
gen=[(m,'Male'),(f,'Female')]
s="s"
M="M"
rel=[(s,'Singale'),(M,'Marrid')]

class profile(models.Model):
    nickname=models.CharField(max_length=50)
    user=models.OneToOneField(User,on_delete='CASCADE')

    dob=models.DateField(null=True)
    phoneno=models.IntegerField()
    gender=models.CharField(choices=gen,max_length=50)
    relation=models.CharField(choices=rel,max_length=50)
    def __str__(self):
        return self.nickname

class frends(models.Model):
        user = models.ForeignKey(profile,max_length=100,on_delete='CASCADE')
        profile= models.ManyToManyField(profile,max_length=50)
        status = models.BooleanField(default=False)


class post(models.Model):
    post_details=models.TextField(max_length=300)

    created_at=models.DateField(auto_now_add=True)
    user=models.OneToOneField(User,on_delete='CASCADE')
    def __str__(self):
        return self.post_d

class tag(models.Model):
    post=models.ForeignKey(post,on_delete='CASCADE')
    tag=models.ManyToManyField(frends)
