from django.db import models

# Create your models here.
# <app>/models.py -> ex. api/models.py
from django import forms

Grade_CHOICES = [
    ('A', ('A')),
    ('B', ('B')),
    ('C', ('C')),
]

class Student(models.Model):
    first_name = models.CharField(blank=True, max_length=255)
    last_name = models.CharField(blank=True, max_length=255)
    age = models.IntegerField(blank=True, null=True)
    grade = models.CharField(blank=True, choices=Grade_CHOICES, max_length=255)
    file = models.FileField(blank=False, upload_to='uploads/', )
    # photo = models.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), upload_to='uploads/', )


class Medical(models.Model):
    name = models.CharField(max_length=22)
    bloodgroup = models.CharField(max_length=22)