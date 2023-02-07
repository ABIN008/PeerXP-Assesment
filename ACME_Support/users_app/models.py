from django import forms
from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)
    desc=models.CharField(max_length=150)
    Created_by=models.CharField(max_length=150)
    Created_at=models.CharField(max_length=150)
    Last_Updated_at=models.CharField(max_length=150)

    def __str__(self):
        return self.name



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    description = models.CharField( max_length=150)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject