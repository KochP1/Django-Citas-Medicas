from django.db import models
from patients.models import Patient
from doctors.models import Doctor

# Create your models here.

class Appointments(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='doctor_appointment', on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, related_name='patient_appointment', on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    notes = models.TextField()
    status = models.CharField(max_length=100)

class MedicalNote(models.Model):
    appointment = models.ForeignKey(Appointments, related_name='medical_notes', on_delete=models.CASCADE)
    note = models.TextField()
    date = models.DateField()

