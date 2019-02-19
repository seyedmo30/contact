from django.db import models
from django.contrib.auth.models import User


class Grp(models.Model):
    name=models.CharField(max_length=30)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Phone(models.Model):


    name=models.CharField(max_length=30)
    number=models.IntegerField(12)
    group=models.ForeignKey(Grp,null='true' ,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
