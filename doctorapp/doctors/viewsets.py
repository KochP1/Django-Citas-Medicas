from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import DoctorSerializer
from .models import Doctor
from .permissions import IsDoctor

from rest_framework.permissions import IsAuthenticatedOrReadOnly

class DoctorViewset(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsDoctor)

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