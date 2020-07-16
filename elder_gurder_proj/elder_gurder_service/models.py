
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    REQUIRED_FIELDS = ['username'] 
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
    
    def __str__(self):
        return self.email



# Create your models here.
class ToDoList(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        verbose_name='user',
        on_delete=models.CASCADE)
    header = models.CharField(max_length=150)
    task = models.TextField(null=True)
    
    def __str__(self):
        return self.header

class Item(models.Model):
    ToDoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
    