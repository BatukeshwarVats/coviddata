from django.db import models

# Create your models here.
class Info(models.Model):
    name=models.CharField(max_length=30)
    contact=models.CharField(max_length=30, default="")
    city=models.CharField(max_length=30, default="")
    tags=models.CharField(max_length=20, default="")
    state=models.CharField(max_length=30, default="")

    def __str__(self):
        return self.name 

class ContactForm(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30, default="")
    contact=models.CharField(max_length=50, default="")
    message=models.CharField(max_length=30, default="")


    def __str__(self):
        return self.fname