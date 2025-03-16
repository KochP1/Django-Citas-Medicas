from django.shortcuts import render
from .serializers import PatientSerializer
from .models import Patient
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

# GET /api/patients => Listar
# POST /api/patients => Crear
# GET /api/patients/<pk> => Detalle
# PUT /api/patients => Modificar

class ListPatients(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST', 'HEAD', 'OPTIONS']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class DetailPatients(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
