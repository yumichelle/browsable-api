from django.shortcuts import render

# Create your views here.
# <app>/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .models import *
from .serializers import *

from modeldir.api import API

# data_api = API(input, outout)

class StudentList(generics.GenericAPIView):
# class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        return Response(StudentList.queryset.values(), status=status.HTTP_200_OK)

    def put(self, request):
        '''
        (type(request.data))
        <class 'django.http.request.QueryDict'>

        (request) 
        <rest_framework.request.Request: PUT '/app/studentlist'>

        (request.data)
        <QueryDict: {'first_name': ['b'], 'last_name': ['m'], 
        'grade': ['A'], 'age': ['1'], 
        'photo': [<InMemoryUploadedFile: s-l640.jpg (image/jpeg)>]}>

        dict(request.data)['photo'] or request.FILES['myfile']?
        [<InMemoryUploadedFile: data.csv (application/vnd.ms-excel)>] 
        InMemoryUploadedFile is a wrapper around a file object. 


        (Student.objects.filter(pk=pk).values()) 
        <QuerySet [{'id': 5, 'first_name': 'm', 'last_name': 'n', 'age': 3, 'grade': 'C', 'photo': 'uploads/data_ssqQyEb.csv'}]>
   

        file_in_memory = Student.objects.filter(pk=pk).values()
        file_object = file_in_memory[0]['photo'] # gets csv
        uploads/data_ssqQyEb.csv

        '''
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            file = dict(request.data)['photo']
            # open file to turn into df:
            open_file(request.FILES['photo'])
            # print(type(data), '\n', data)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # way 2


class StudentDetail(APIView):
# class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, pk, *args, **kwargs):
        open_file(dict(request.data), pk)
        return Response(Student.objects.filter(pk=pk).values(), status=status.HTTP_200_OK)






@api_view(['POST'])
def save_medical(request):
    name = request.POST.get('name')
    bloodgroup = request.POST.get('bloodgroup')

    try:
        Medical.objects.create(name= name, bloodgroup = bloodgroup)
        return Response("Data Saved!", status=status.HTTP_201_CREATED)

    except Exception as ex:
        return Response(ex, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_medical(request):
    return Response(Medical.objects.all().values(), status=status.HTTP_200_OK)


import io
import csv
import pandas as pd
def open_file(file, pk):

    print (Student.objects.filter(pk=pk).values()) # <QuerySet [{'id': 5, 'first_name': 'm', 'last_name': 'n', 'age': 3, 'grade': 'C', 'photo': 'uploads/data_ssqQyEb.csv'}]>
    file_in_memory = Student.objects.filter(pk=pk).values()
    file_object = file_in_memory[0]['photo'] # gets csv
    print(file_object)

    df = pd.read_csv(file_object)
    print (df)