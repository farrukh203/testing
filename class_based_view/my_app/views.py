from django.shortcuts import render
from .models import Students
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.core import serializers

# Create your views here.


class StudentList(APIView):
    """
    View to list all students in the Student Model
    * Requires BasicAuthentication
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        returns a list of all students
        """
        #queryset = Students.objects.all()
        #q = [s.stu_name for s in Students.objects.all()]
        #print(q)
        data = serializers.serialize("json", Students.objects.all())
        return Response(data)

