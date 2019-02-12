from django.db import models
from .models import Grp
from django.contrib.auth.models import User

class Phone(models.Model):


    name=models.CharField(max_length=30)
    number=models.IntegerField()
    group=models.ForeignKey(Grp,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Grp(models.Model):
    name=models.CharField(max_length=30)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
