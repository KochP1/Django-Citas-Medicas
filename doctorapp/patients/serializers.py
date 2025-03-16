from rest_framework import serializers
from .models import Patient, Insurance, MedicalRecord
from bookings.serializers import AppointmentsSerializer
from datetime import date

class PatientSerializer(serializers.ModelSerializer):
    appointments = AppointmentsSerializer(many=True, read_only=True, source='patient_appointment')
    age = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = [
            'id',
            'first_name',
            'last_name',
            'age',
            'date_of_birth',
            'contact_number',
            'email',
            'adress',
            'medical_history',
            'appointments',
        ]
    
    def get_age(self, obj):
        age_td = date.today() - obj.date_of_birth
        return age_td.days // 365

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'