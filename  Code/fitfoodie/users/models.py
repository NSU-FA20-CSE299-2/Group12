from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Profile(AbstractUser):
    age = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    bmi = models.PositiveIntegerField()


