from django.db import models

# Create your models here.
class Author(models.Model):
    Aid=models.IntegerField(primary_key=True,auto_created=True,null=False)
    Aname=models.CharField(max_length=80)
    Adob=models.DateField()
    def __str__(self):
        return self.Aname
class Post(models.Model):
    pid=models.IntegerField(primary_key=True,auto_created=True,null=False)
    title=models.CharField(max_length=80)
    Author=models.ForeignKey(to=Author,on_delete='CASCADE')
    post=models.TextField(max_length=200)
    cdate=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title

