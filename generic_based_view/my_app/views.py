from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from .serializer import StudentSerializer
from .models import Students, Course, Grade

# Create your views here.


class StudentList(generics.ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)


class StudentCreate(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentRetrieve(generics.RetrieveAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = self.queryset.filter(id=kwargs['pk'])
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)
