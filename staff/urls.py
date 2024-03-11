from django.urls import path
from . import views
from .views import MainPageView, analytics, CallbackView, DoctorAppointmentView, AppointmentHistoryView


urlpatterns = [
    path('main/', MainPageView.as_view(), name='AdminMain'),
    path('analytics/', views.analytics, name='Analytics'),
    path('callback/', CallbackView.as_view(), name='Callback'),
    path('doctor-appointments/<int:doctor_id>/', DoctorAppointmentView.as_view(), name='DocAnalytics'),
    path('appointment-history', AppointmentHistoryView.as_view(), name='AppHistory'),
]
