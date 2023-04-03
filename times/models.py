from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class userModel(AbstractUser):
    phone = models.CharField(max_length=10)
    role = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    nationality = models.CharField(max_length=300)
