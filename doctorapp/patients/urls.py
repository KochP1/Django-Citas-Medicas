from django.urls import path
from .views import ListPatients, DetailPatients, ListInsurance, DetailInsurance, ListMeicalRecord, DetailMedicalRecord

urlpatterns = [
    path('patients', ListPatients.as_view(), name='list_patients'),
    path('patients/<int:pk>/', DetailPatients.as_view()),
    path('patients/insurance', ListInsurance.as_view()),
    path('patients/insurance/<int:pk>/', DetailInsurance.as_view()),
    path('patients/medical_record', ListMeicalRecord.as_view()),
    path('patients/medical_record/<int:pk>/', DetailMedicalRecord.as_view())
]
