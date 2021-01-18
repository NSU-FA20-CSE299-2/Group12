from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Profile(AbstractUser):
    age = models.CharField(max_length=5, blank=True)
    weight = models.CharField(max_length=5, blank=True)
    height = models.CharField(max_length=5, blank=True)
    bmi = models.CharField(max_length=5, blank=True)


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
