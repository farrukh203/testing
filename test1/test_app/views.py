from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Person, Group, Membership
from rest_framework import generics
from .serializer import PersonSerializer, GroupSerializer, MembershipSerializer

# Create your views here.


class PersonListCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PersonSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = self.queryset.filter(id=kwargs['pk']).get()
        serializer = PersonSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        person = self.queryset.filter(id=kwargs['pk']).get()
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Person data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        person = self.queryset.filter(id=kwargs['pk']).get()
        serializer = PersonSerializer(person, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Person date partially updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        person = self.queryset.filter(id=kwargs['pk']).get()
        person.delete()
        return Response({'msg': 'Person data deleted'}, status=status.HTTP_204_NO_CONTENT)


class GroupListCreateView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = GroupSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = self.queryset.filter(id=kwargs['pk']).get()
        serializer = GroupSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        group = self.queryset.filter(id=kwargs['pk']).get()
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Group data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        group = self.queryset.filter(id=kwargs['pk']).get()
        serializer = GroupSerializer(group, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Group date partially updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        group = self.queryset.filter(id=kwargs['pk']).get()
        group.delete()
        return Response({'msg': 'Group data deleted'}, status=status.HTTP_204_NO_CONTENT)


class MembershipListCreateView(generics.ListCreateAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = MembershipSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = MembershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MembershipRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

    def retrieve(self, request, *args, **kwargs):
        member = self.queryset.filter(id=kwargs['pk']).get()
        serializer = MembershipSerializer(member)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        member = self.queryset.filter(id=kwargs['pk']).get()
        serializer = MembershipSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Group data updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        member = self.queryset.filter(id=kwargs['pk']).get()
        serializer = MembershipSerializer(member, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Group date partially updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        member = self.queryset.filter(id=kwargs['pk']).get()
        member.delete()
        return Response({'msg': 'Group data deleted'}, status=status.HTTP_204_NO_CONTENT)
