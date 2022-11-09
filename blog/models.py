from email import message
from turtle import title
from django.db import models

# Create your models here.
class Blog_page(models.Model):
    title = models.CharField(max_length=100)
    message = models.CharField(max_length=300)
    body = models.TextField

    def __str__(self):
        return self.title