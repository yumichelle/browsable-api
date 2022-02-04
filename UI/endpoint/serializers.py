# <app>/serializers.py -> ex. api/serializers.py
from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'grade', 'age', 'photo')

class MedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical
        fields = ('name', 'bloodgroup',)