from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from .serializer import StudentSerializer
from .models import Students, Course, Grade
from datetime import datetime

# Create your views here.


class StudentAPI(APIView):

    def get(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Students.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = Students.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        id = pk
        stu = Students.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        id = pk
        stu = Students.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        id = pk
        stu = Students.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Student is deleted'}, status=status.HTTP_204_NO_CONTENT)


class StudentList(generics.ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)


class StudentCreate(generics.CreateAPIView):

    def create(self, request, *args, **kwargs):
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


class StudentUpdate(generics.UpdateAPIView):

    def put(self, request, *args, **kwargs):
        Students.objects.filter(id=kwargs['pk']).update(stu_updated_at=datetime.now())
        stu = Students.objects.get(id=kwargs['pk'])
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        stu = Students.objects.get(id=kwargs['pk'])
        # request.data['stu_updated_at'] = datetime.now()
        # data = request.data
        # data['stu_updated_at'] = datetime.now()
        # # data['stu_updated_at'] = datetime.now()
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            # serializer.validated_data['stu_updated_at'] = datetime.now()
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDelete(generics.DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        stu = Students.objects.get(id=kwargs['pk'])
        stu.delete()
        return Response({'msg':'Student data deleted'}, status=status.HTTP_204_NO_CONTENT)
