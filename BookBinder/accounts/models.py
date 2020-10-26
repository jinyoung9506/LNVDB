from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length = 13, blank = True)
    title = models.CharField(max_length = 200, blank = True)
    booklink = models.CharField(max_length = 200, blank = True)
    imagelink = models.CharField(max_length = 200, blank = True)
    author = models.CharField(max_length = 200, blank = True)
    price = models.CharField(max_length = 200, blank = True)
    publisher = models.CharField(max_length = 200, blank = True)
    date = models.CharField(max_length = 200, blank = True)
    memo = models.CharField(max_length = 200, blank = True)
    before = models.CharField(max_length = 200, blank = True)
    after = models.CharField(max_length = 200, blank = True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    books = models.ForeignKey(Book, on_delete = models.CASCADE, blank = True)

    

