# <app>/serializers.py -> ex. api/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # read_only_fields = ('pk', 'first_name', 'last_name', 'grade', 'age')
        fields = ('pk', 'first_name', 'last_name', 'grade', 'age', 'file')
#         owner = serializers.ReadOnlyField(source='owner.username')


# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'endpoint']


# class MedicalSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Medical
#         fields = ('name', 'bloodgroup',)