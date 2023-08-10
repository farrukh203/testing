from rest_framework import serializers
from .models import Person, Group, Membership


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ['name', 'age']


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['group_name', 'members']


class MembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Membership
        fields = ['person', 'group', 'date_joined', 'invite_reason']
