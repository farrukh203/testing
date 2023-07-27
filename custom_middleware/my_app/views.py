from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse

# Create your views here.


def my_view(request):
    print("This is my view")
    return HttpResponse("This is home page of my site")


def exception_view(request):
    variable_x = 10/0
    return HttpResponse("This is exception_view response")


def student_info(request):
    print("I am a User info view")
    context = {'name':'ali'}
    return TemplateResponse(request, "my_app/my_template.html", context)


def student_detail(request):
    context = {'name': 'abc'}
    return TemplateResponse(request, "my_app/my_template.html", context)
