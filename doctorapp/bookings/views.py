from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Appointments, MedicalNote
from .serializers import AppointmentsSerializer, MedicalNoteSerializer


# Create your views here.

# BOOKINGS
class ListBookings(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST', 'HEAD', 'OPTIONS']
    serializer_class = AppointmentsSerializer
    queryset = Appointments.objects.all()

class DetailBookings(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = AppointmentsSerializer
    queryset = Appointments.objects.all()


# MEDICAL NOTES
class ListMedicalNotes(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST', 'HEAD', 'OPTIONS']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()

class DetailMedicalNotes(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()
