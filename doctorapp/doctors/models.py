from django.db import models

# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    adress = models.TextField()
    biography = models.TextField(max_length=100)
    is_on_vacation = models.BooleanField(default=False)

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)

class DoctorAvailabity(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='availabities', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

class MedicalNote(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='medical_notes', on_delete=models.CASCADE)
    note = models.TextField()
    date = models.DateField()