from django.db import models

# Create your models here.
class Challan(models.Model):
    issueid = models.CharField(max_length=20,primary_key = True)
    pemail = models.CharField(max_length=20)
    demail = models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    reason = models.CharField(max_length=20)
    status = models.CharField(max_length=20,default = 'Pending', blank = False)
    fine = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

class Police(models.Model):
    email = models.CharField(max_length=20)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
