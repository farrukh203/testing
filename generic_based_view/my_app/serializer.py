from rest_framework import serializers
from .models import Students, Course, Grade
import datetime


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = ['id', 'first_name', 'last_name', 'age', 'gender', 'address', 'standard',
                  'course', 'father_name', 'parent_contact_number', 'stu_updated_at']

    # def update(self, instance, validated_data):
    #     instance.stu_updated_at = validated_data.get('stu_updated_at', datetime.datetime.now())
    #     instance.save()
    #     return instance
