# <app>/serializers.py -> ex. api/serializers.py
from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # read_only_fields = ('pk', 'first_name', 'last_name', 'grade', 'age')
        fields = ('pk', 'first_name', 'last_name', 'grade', 'age', 'file')

class MedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical
        fields = ('name', 'bloodgroup',)