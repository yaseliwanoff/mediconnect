from django.urls import path
from . import views
from .views import DoctorInfo, DoctorListView, RegisterFormView, LoginUserView, my_logout_view,\
    UserPageView, Main, ContactView, cancel_appointment


urlpatterns = [
    path('', Main.as_view(), name='Home'),
    path('doctor-info/<int:doctor_id>/', DoctorInfo.as_view(), name='DocInfo'),
    path('register/', RegisterFormView.as_view(), name='Register'),
    path('login/', LoginUserView.as_view(), name='Login'),
    path('logout/', my_logout_view, name='Logout'),
    path('my-page/', UserPageView.as_view(), name='UserPage'),
    path('doctor-list/', DoctorListView.as_view(), name='DoctorList'),
    path('contacts/', views.ContactView, name='Contact'),
    path('cancel-appointment/<int:appointment>/', views.cancel_appointment, name='Cancel'),
]