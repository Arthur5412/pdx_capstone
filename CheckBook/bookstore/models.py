import email
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#this creates the book model and set the fields to it, this stores information about the book
class Book(models.Model):
    Title =models.CharField(max_length=120, null=True)
    Author =models.CharField(max_length=120, null=True)
    Summary =models.CharField(max_length=120, null=True)
    Language =models.CharField(max_length=40, null=True)
    Edition=models.IntegerField()

    #returns information in a string in this order of title first and edition second 
    def __str__(self):
        return f"{self.Title}   :   {self.Author}   :   {self.Edition}"
        

#we create a user class which will store information about Members
class Member(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120, null=True)
    last_name = models.CharField(max_length=120,null = True)
    phone = models.CharField(max_length=120, null=True)
    email=models.CharField(max_length=120, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    #returns information in a string in this order
    def __str__(self):
        return f"{self.first_name}   :   {self.last_name}   :  {self.date_created}"
      


#we create a cart class which stores books added by the member
class Cart(models.Model):
    member = models.OneToOneField(Member,null=True, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)











