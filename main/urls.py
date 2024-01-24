from django.urls import path, include
from django.shortcuts import render
from .views import DoctorInfo, DoctorList

urlpatterns = [
    path('', DoctorList.as_view(), name='DoctorList'),
    path('doctor-info/<int:doctor_id>/', DoctorInfo.as_view(), name='DocInfo'),
    # path('select-appointment', SelectAppoint.as_view(), name='SelectAppoint')
]