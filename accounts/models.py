from django.db import models
from django.contrib import auth
from django.contrib.auth.models import AbstractUser


# Create your models here.
class stu(AbstractUser):
    student = models.CharField(max_length=30, verbose_name="Student ID")
    def __str__(self):
        return f"{self.username}"


# class User(auth.models.User, auth.models.PermissionsMixin):
    

	# def __str__(self):
    # 		return f"{self.username}"
