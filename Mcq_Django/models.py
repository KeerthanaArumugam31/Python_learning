from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    mobilenumber=models.CharField(max_length=50,default="********")
    password=models.CharField(max_length=20)

class Questions(models.Model):
    question=models.CharField(max_length=200)
    optiona=models.CharField(max_length=50)
    optionb = models.CharField(max_length=50)
    optionc = models.CharField(max_length=50)
    answer= models.CharField(max_length=50)



