from django.db import models

# Create your models here.
# <app>/models.py -> ex. api/models.py

Grade_CHOICES = [
    ('A', ('A')),
    ('B', ('B')),
    ('C', ('C')),
]

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    grade = models.CharField(choices=Grade_CHOICES, max_length=255)
    photo = models.FileField(blank=False, upload_to='uploads/', )


class Medical(models.Model):
    name = models.CharField(max_length=22)
    bloodgroup = models.CharField(max_length=22)