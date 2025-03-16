from rest_framework import serializers
from doctors.models import Doctor, DoctorAvailabity ,MedicalNote, Department
from bookings.serializers import AppointmentsSerializer

class DoctorSerializer(serializers.ModelSerializer):
    appointments = AppointmentsSerializer(many=True, read_only=True, source='doctor_appointment')
    class Meta:
        model = Doctor
        fields = [
            'id',
            'first_name',
            'last_name',
            'qualification',
            'contact_number',
            'email',
            'adress',
            'biography',
            'is_on_vacation',
            'appointments'
        ]
    
    def validate_email(self, value):

        if '@example.com' in value:
            return value
        
        raise serializers.ValidationError('El correo debe incluir @example.com')
    
    def validate(self, attrs):
        attrs['email']
        if len(attrs['contact_number']) > 10 and attrs['is_on_vacation'] == True:
            raise serializers.ValidationError('Por favor ingresa un numero valido antes de irte de vacaciones')
        return super().validate(attrs)

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