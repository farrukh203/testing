"""
URL configuration for generic_based_view project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_list/', views.StudentList.as_view()),
    path('student_create/', views.StudentCreate.as_view()),
    path('student_retrieve/<int:pk>', views.StudentRetrieve.as_view()),
    path('student_update/<int:pk>', views.StudentUpdate.as_view()),
    path('student_delete/<int:pk>', views.StudentDelete.as_view()),
    #path('student_delete/<int:pk>', views.StudentDelete.as_view()),
    path('student_api/', views.StudentAPI.as_view()),
    path('student_api/<int:pk>', views.StudentAPI.as_view())
]