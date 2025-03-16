from django.urls import path
from .views import list_doctors, detail_doctors

urlpatterns = [
    path('doctors', list_doctors, name='list_doctors'),
    path('doctors/<int:pk>/', detail_doctors, name='detail_doctors')
]
