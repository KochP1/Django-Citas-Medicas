from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ListDoctors, DetailDoctors, ListDepartment, DetailDepartment, ListAvailability, DetailAvailability, ListMedicalNotes, DetailMedicalNotes
from .viewsets import DoctorViewset

routers = DefaultRouter()
routers.register('doctors', DoctorViewset)

urlpatterns = [
] + routers.urls
