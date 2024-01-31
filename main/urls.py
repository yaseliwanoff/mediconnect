from django.urls import path
from .views import DoctorInfo, DoctorList, RegisterFormView, LoginUserView, my_logout_view


urlpatterns = [
    path('', DoctorList.as_view(), name='Home'),
    path('doctor-info/<int:doctor_id>/', DoctorInfo.as_view(), name='DocInfo'),
    path('register/', RegisterFormView.as_view(), name='Register'),
    path('login/', LoginUserView.as_view(), name='Login'),
    path('logout/', my_logout_view, name='Logout'),
]