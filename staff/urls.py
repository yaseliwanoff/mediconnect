from django.urls import path
from . import views
from .views import MainPageView, ChatView, analytics, callback, RoomView, DoctorAnalyticsView


urlpatterns = [
    path('main/', MainPageView.as_view(), name='AdminMain'),
    path('chat/', ChatView.as_view(), name='Chat'),
    path('analytics/', views.analytics, name='Analytics'),
    path('callback/', views.analytics, name='Callback'),
    path('<int:room_id>/', RoomView.as_view(), name="Room"),
    path('doctor-analytics/<int:doctor_id>/', DoctorAnalyticsView.as_view(), name='DocAnalytics'),
]
