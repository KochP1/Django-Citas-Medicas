from django.shortcuts import render
from .models import Doctor, DoctorAvailabity, MedicalNote, Department
from .serializers import DoctorSerializer, DepartmentSerializer, MedicalNoteSerializer, DoctorAvailabitySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.

# GENERICS 

# DOCTORS
class ListDoctors(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST', 'HEAD', 'OPTIONS']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class DetailDoctors(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


# DEPARTMENT
class ListDepartment(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST', 'HEAD', 'OPTIONS']
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

class DetailDepartment(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

# DOCTOR AVAILABILITY
class ListAvailability(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST', 'HEAD', 'OPTIONS']
    serializer_class = DoctorAvailabitySerializer
    queryset = DoctorAvailabity.objects.all()

class DetailAvailability(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorAvailabitySerializer
    queryset = DoctorAvailabity.objects.all()

# MEDICAL NOTES
class ListMedicalNotes(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST', 'HEAD', 'OPTIONS']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()

class DetailMedicalNotes(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()