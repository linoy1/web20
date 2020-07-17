
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    username = models.CharField(max_length=255)
    REQUIRED_FIELDS = [''] 
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
    
    def __str__(self):
        return self.email


# lonely
# Create your models here.
class LonelyPeople(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        verbose_name='user',
        on_delete=models.CASCADE)
    name    = models.CharField(max_length=150)
    age     = models.IntegerField()
    address = models.CharField(max_length=150)
    phone   = models.CharField(max_length=20)
    deatils = models.TextField(null=True)
    
    def __str__(self):
        return f'The name is {self.name} and his address is {self.address}'

class Visitis(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        verbose_name='user',
        related_name="visitor",
        on_delete=models.CASCADE)
    loneny = models.ForeignKey(
        LonelyPeople(),
        verbose_name='loneny',
        related_name="visited",
        on_delete=models.CASCADE)
    date = models.DateField(verbose_name='data')
    visit_details = models.TextField(null=True)
    
    def __str__(self):
        return f'{self.user} visit {self.loneny} at {self.date}'


