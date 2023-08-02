from rest_framework import serializers
from .models import Students, Course, Grade


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'first_name', 'last_name', 'age', 'gender', 'address', 'standard',
                  'course', 'father_name', 'parent_contact_number']
