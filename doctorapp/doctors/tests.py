from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from patients.models import Patient
from doctors.models import Doctor
# Create your tests here.

class DoctorViewsetTests(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            first_name = 'Maria',
            last_name = 'Koch',
            date_of_birth = '2000-07-09',
            contact_number = '303001',
            email = 'maria@example.com',
            adress = 'prueba',
            medical_history = 'Ninguna',
        )

        self.doctor = Doctor.objects.create(
            first_name = 'Edagr',
            last_name = 'Leon',
            qualification = '2000-07-09',
            contact_number = '1015145',
            email = 'edgar@example.com',
            adress = 'prueba',
            biography = 'Ninguna',
            is_on_vacation = False,
        )

        self.client = APIClient()
    
    def test_list_should_return_200(self):
        url = reverse(
            'doctor-appointments', 
            kwargs={'pk': self.doctor.id}
            )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


