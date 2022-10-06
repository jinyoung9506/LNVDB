from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Book(models.Model):
    objects = models.Manager()

    owner = models.CharField(max_length = 200, blank = False)
    isbn = models.CharField(max_length = 200, blank = False)
    title = models.CharField(max_length = 200, blank = True)
    booklink = models.CharField(max_length = 200, blank = True)
    author = models.CharField(max_length = 200, blank = True)
    price = models.CharField(max_length = 200, blank = True)
    publisher = models.CharField(max_length = 200, blank = True)
    date = models.CharField(max_length = 200, blank = True)
    imagelink = models.CharField(max_length = 200, blank = True)
    memo = models.CharField(max_length = 200, blank = True, null = False)

    class Meta:
        unique_together = (("owner", "isbn"),)
