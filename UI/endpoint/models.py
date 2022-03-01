from django.db import models

# Create your models here.
# <app>/models.py -> ex. api/models.py
from django.contrib.auth.models import User
from rest_framework import generics
from django.conf import settings

Grade_CHOICES = [
    ('A', ('A')),
    ('B', ('B')),
    ('C', ('C')),
]

class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                        default = 1,
                        null = True, 
                        on_delete = models.SET_NULL,
                        )
    first_name = models.CharField(blank=True, max_length=255)
    last_name = models.CharField(blank=True, max_length=255)
    age = models.IntegerField(blank=True, null=True)
    grade = models.CharField(blank=True, choices=Grade_CHOICES, max_length=255)
    file = models.FileField(blank=False, upload_to='uploads/', )
    # photo = models.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), upload_to='uploads/', )

    # def save(self, *args, **kwargs):
    #     """
    #     Use the `pygments` library to create a highlighted HTML
    #     representation of the code snippet.
    #     """
    #     lexer = get_lexer_by_name(self.language)
    #     linenos = 'table' if self.linenos else False
    #     options = {'title': self.title} if self.title else {}
    #     formatter = HtmlFormatter(style=self.style, linenos=linenos,
    #                             full=True, **options)
    #     self.highlighted = highlight(self.code, lexer, formatter)
    #     super().save(*args, **kwargs)





# class Medical(models.Model):
#     name = models.CharField(max_length=22)
#     bloodgroup = models.CharField(max_length=22)