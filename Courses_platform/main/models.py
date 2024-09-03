from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Course(models.Model):
    LEVEL_CHOICES = [
        ("Low level", "Low level"),
        ("High Level", "High Level"),
        ("Advanced Level", "Advanced Level"),
    ]
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.IntegerField()
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="courses")

    def __str__(self):
        return self.name


