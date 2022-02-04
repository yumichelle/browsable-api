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
        print(request.data) # <rest_framework.request.Request: PUT '/app/studentlist'>
        '''
        <QueryDict: {'first_name': ['b'], 'last_name': ['m'], 
        'grade': ['A'], 'age': ['1'], 
        'photo': [<InMemoryUploadedFile: s-l640.jpg (image/jpeg)>]}>
        '''
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # way 2


class StudentDetail(APIView):
# class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        return Response(StudentList.queryset.values(), status=status.HTTP_200_OK)

    def put(self, request):
        print(request)
        if StudentDetail.is_valid(self):
            StudentDetail.save()
            return Response(StudentDetail.data, status=status.HTTP_201_CREATED)
        return Response(StudentDetail.errors, status=status.HTTP_400_BAD_REQUEST) # way 2




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