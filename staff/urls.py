from django.urls import path
from . import views
from .views import MainPageView, ChatView, analytics, callback, RoomView, DoctorAppointmentView, AppointmentHistoryView


urlpatterns = [
    path('main/', MainPageView.as_view(), name='AdminMain'),
    path('chat/', ChatView.as_view(), name='Chat'),
    path('analytics/', views.analytics, name='Analytics'),
    path('callback/', views.analytics, name='Callback'),
    path('<int:room_id>/', RoomView.as_view(), name="Room"),
    path('doctor-appointments/<int:doctor_id>/', DoctorAppointmentView.as_view(), name='DocAnalytics'),
    path('appointment-history', AppointmentHistoryView.as_view(), name='AppHistory'),
]
