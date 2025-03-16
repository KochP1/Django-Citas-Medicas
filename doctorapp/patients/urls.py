from django.urls import path
from .views import ListPatients, DetailPatients

urlpatterns = [
    path('patients', ListPatients.as_view(), name='list_patients'),
    path('patients/<int:pk>/', DetailPatients.as_view())
]
