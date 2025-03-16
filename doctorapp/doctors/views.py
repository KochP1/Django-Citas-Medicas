from django.shortcuts import render
from .models import Doctor, DoctorAvailabity, MedicalNote, Department
from .serializers import DoctorSerializer, DepartmentSerializer, MedicalNoteSerializer, DoctorAvailabitySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def list_doctors(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = DoctorSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status= status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def detail_doctors(request, pk):
    try:
        doctors = Doctor.objects.get(id=pk)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DoctorSerializer(doctors)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = DoctorSerializer(doctors, data = request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    if request.method == 'DELETE':
        doctors.delete()
        return Response(status=status.HTTP_200_OK)