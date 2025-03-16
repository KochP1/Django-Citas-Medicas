from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import DoctorSerializer
from .models import Doctor
from .permissions import IsDoctor
from bookings.serializers import AppointmentsSerializer
from bookings.models import Appointments

from rest_framework.permissions import IsAuthenticated

class DoctorViewset(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = (IsAuthenticated, IsDoctor)

    @action(['POST'], detail=True, url_path='set-on-vacations')
    def set_on_vacations(self, request, pk):
        doctor = self.get_object()

        doctor.is_on_vacation = True
        doctor.save()
        return Response({'status': 'El doctor esta en vacaciones'})
    
    @action(['POST'], detail=True, url_path='set-off-vacations')
    def set_off_vacations(self, request, pk):
        doctor = self.get_object()

        doctor.is_on_vacation = False
        doctor.save()
        return Response({'status': 'El doctor no esta en vacaciones'})
    
    @action(['POST', 'GET', 'DELETE'], detail=True, serializer_class=AppointmentsSerializer)
    def appointments(self, request, pk):
        doctor = self.get_object()
        if request.method == 'POST':
            data = request.data.copy()
            data['doctor'] = doctor.id
            serializer = AppointmentsSerializer(data = data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        if request.method == 'GET':
            appointments = Appointments.objects.filter(doctor = doctor)
            serializer = AppointmentsSerializer(appointments, many=True)
            return Response(serializer.data)
        
        if request.method == 'DELETE':
            appointments = Appointments.objects.filter(doctor = doctor)
            appointments.delete()
            return Response(status=status.HTTP_200_OK)
