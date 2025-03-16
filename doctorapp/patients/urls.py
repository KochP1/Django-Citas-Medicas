from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ListPatients, DetailPatients, ListInsurance, DetailInsurance, ListMeicalRecord, DetailMedicalRecord
from .viewsets import MedicalRecordViewset


routers = DefaultRouter()
routers.register('patients/medical_record', MedicalRecordViewset)

urlpatterns = [
    path('patients', ListPatients.as_view(), name='list_patients'),
    path('patients/<int:pk>/', DetailPatients.as_view()),
    path('patients/insurance', ListInsurance.as_view()),
    path('patients/insurance/<int:pk>/', DetailInsurance.as_view()),
] + routers.urls
