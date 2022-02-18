from datetime import datetime
from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email= models.EmailField(blank=False,default=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

