from django.urls import path
from .views import ListDoctors, DetailDoctors, ListDepartment, DetailDepartment, ListAvailability, DetailAvailability, ListMedicalNotes, DetailMedicalNotes

urlpatterns = [
    path('doctors', ListDoctors.as_view(), name='list_doctors'),
    path('doctors/<int:pk>/', DetailDoctors.as_view(), name='detail_doctors')
]
