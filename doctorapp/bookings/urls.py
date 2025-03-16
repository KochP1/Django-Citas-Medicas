from django.urls import path
from .views import ListMedicalNotes, ListBookings, DetailBookings, DetailMedicalNotes

urlpatterns = [
    path('bookings', ListBookings.as_view(), name='bookings'),
    path('bookings/<int:pk>/', DetailBookings.as_view(), name='bookings_id'),
    path('bookings/med_notes', ListMedicalNotes.as_view(), name='bookings_med_notes'),
    path('bookings/med_notes/<int:pk>/', DetailMedicalNotes.as_view(), name='bookings_med_notes_id'),
]
