from django.db import models

# Create your models here.
class FileModel(models.Model):
    upload = models.FileField(null=True)