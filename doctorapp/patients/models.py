from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    adress = models.TextField()
    medical_history = models.TextField(null=True)

class Insurance(models.Model):
    patient = models.ForeignKey(Patient, related_name='insurance', on_delete=models.CASCADE)
    provider = models.CharField(max_length=100)
    policiy_number = models.CharField(max_length=100)
    expiration_date = models.DateField()

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, related_name='medical_record', on_delete=models.CASCADE)
    date = models.DateField()
    diagnosis = models.TextField(max_length=100)
    treatment = models.TextField(max_length=100)
    follow_up_date = models.DateField()
