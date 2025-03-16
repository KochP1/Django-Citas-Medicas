from rest_framework import serializers
from doctors.models import Doctor, DoctorAvailabity ,MedicalNote, Department

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DoctorAvailabitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailabity
        fields = '__all__'

class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = '__all__'