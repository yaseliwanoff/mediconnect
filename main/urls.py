from django.urls import path
from . import views
from .views import DoctorInfo, DoctorListView, RegisterFormView, LoginUserView, my_logout_view,\
    UserAppointmentsListView, Main, ContactView


urlpatterns = [
    path('', Main.as_view(), name='Home'),
    path('doctor-info/<int:doctor_id>/', DoctorInfo.as_view(), name='DocInfo'),
    path('register/', RegisterFormView.as_view(), name='Register'),
    path('login/', LoginUserView.as_view(), name='Login'),
    path('logout/', my_logout_view, name='Logout'),
    path('my-appointments/', UserAppointmentsListView.as_view(), name='UserAppointments'),
    path('doctor-list/', DoctorListView.as_view(), name='DoctorList'),
    path('contacts/', views.ContactView, name='Contact')
]