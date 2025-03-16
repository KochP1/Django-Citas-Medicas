from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from .serializers import MedicalRecordSerializer
from .models import MedicalRecord

class MedicalRecordViewset(viewsets.ModelViewSet):
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()

    @action(['GET'], detail=True, url_path='get-patient-record')
    def get_patient_record(self, request, pk):
        try:
            record = self.get_object()
        except MedicalRecord.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(record)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        
    
    @action(['POST'], detail=False, url_path='post-patient-record')
    def post_patient_record(self, request, pk):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid()
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
