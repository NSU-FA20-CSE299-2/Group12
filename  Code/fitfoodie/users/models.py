from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Profile(AbstractUser):
    age = models.CharField(max_length=5, blank=True)
    weight = models.CharField(max_length=5, blank=True)
    height = models.CharField(max_length=5, blank=True)
    bmi = models.CharField(max_length=5, blank=True)
