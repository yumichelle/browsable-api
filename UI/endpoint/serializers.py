# <app>/serializers.py -> ex. api/serializers.py
from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # read_only_fields = ('pk', 'first_name', 'last_name', 'grade', 'age')
        fields = ('pk', 'first_name', 'last_name', 'grade', 'age', 'file')

# class FileListSerializer ( serializers.Serializer ) :
#     image = serializers.ListField(
#                        child=serializers.FileField( max_length=100000,
#                                          allow_empty_file=False,
#                                          use_url=False )
#                                 )
#     def create(self, validated_data):
#         blogs=Student.objects.latest()
#         image=validated_data.pop('file')
#         for img in image:
#             photo=Student.objects.create(image=img,blogs=blogs,**validated_data)
#         return photo

class MedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical
        fields = ('name', 'bloodgroup',)