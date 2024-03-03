from django.urls import path
from . import views
from .views import Main, ChatView, analytics, callback, RoomView


urlpatterns = [
    path('main/', Main.as_view(), name='AdminMain'),
    path('chat/', ChatView.as_view(), name='Chat'),
    path('analytics/', views.analytics, name='Analytics'),
    path('callback/', views.analytics, name='Callback'),
    path('<int:room_id>/', RoomView.as_view(), name="Room"),
]
