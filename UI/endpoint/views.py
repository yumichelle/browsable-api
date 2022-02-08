from django.shortcuts import render

# Create your views here.
# <app>/views.py
from rest_framework import generics, parsers, renderers, serializers, status
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.decorators import action, api_view

from .models import *
from .serializers import *

from ModelDir.api import API
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class StudentList(generics.ListCreateAPIView):
    """ StudentList shows all records in Student database when at path, /studentlist. """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)

    def get(self, request):
        """
        Return all records in Student database by default when at path, /studentlist.

        :param self: <class 'endpoint.views.StudentList'>
        :param request: {}
        :return: returns all records in Student database.
        """
        return Response(StudentList.queryset.values(), status=status.HTTP_200_OK)

    def put(self, request):
        """
        A PUT request to submit a record in Student database. A request to the API is called.

        :param self: <class 'endpoint.views.StudentList'>
        :param request: a QueryDict, a dictionary, with values from the PUT request.
        :return: returns the record added in Student database if StudentSerializer is valid.
        """
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # print ('StudentList PUT', dict(request.data)) #  {'first_name': ['b'], 'last_name': ['m'], 'grade': ['A'], 'age': [''], 'file': [<InMemoryUploadedFile: data.csv (application/vnd.ms-excel)>]}
            open_file(serializer.data['pk'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            open_file(serializer.data['pk'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    """ StudentDetail shows a specific record in Student database when at path, /<int:pk>. """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, pk, *args, **kwargs):
        """
        Done by default. A request to the API is called.

        :param self: <class 'endpoint.views.StudentDetail'>
        :param request: {}
        :param pk: primary key based on path, /<int:pk>.
        :return: returns a specific record in Student database.
        """
        open_file(pk)
        return Response(Student.objects.filter(pk=pk).values(), status=status.HTTP_200_OK)
    
    def delete(self, request, pk, format=None):
        """
        Delete record at path, /<int:pk>.

        :param self: <class 'endpoint.views.StudentDetail'>
        :param request: {}
        :param pk: primary key based on path, /<int:pk>.
        :return: returns a specific record in Student database.
        """
        # https://stackoverflow.com/questions/9143262/delete-multiple-objects-in-django
        return Response(Student.objects.filter(pk=pk).delete(), status=status.HTTP_204_NO_CONTENT)



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




def open_file(pk):
    """
    Makes the call to the API, api.py.

    :param requestData: {} <- when called from StudentDetail GET.
                        {'first_name': ['b'], 'last_name': ['m'], 'grade': ['A'], 'age': [''], 'file': [<InMemoryUploadedFile: data.csv (application/vnd.ms-excel)>]} <- when called from StudentList PUT.
    :param pk: primary key based on path, /<int:pk>.
    """
    # get the QuerySet object if the pk matches the pk argument:
    file_in_memory = Student.objects.filter(pk=pk).values()
    # gets csv:
    file_object = file_in_memory[0]['file']
    print('open_file() has', file_object)

    # if the file is a csv:
    if file_object.endswith(".csv"):
        print("using api.py")
        input = file_object
        output = '../modeldir/output/'
        # make the API instance and pass in the input and output. Call main() in api.py: 
        data_api = API(input, output)
        data_api.main()

    else: 
        print("this isn't a csv file")