from django.urls import path
from . import views
from .views import Main, chat, analytics, callback


urlpatterns = [
    path('main/', Main.as_view(), name='AdminMain'),
    path('chat/', views.chat, name='Chat'),
    path('analytics/', views.analytics, name='Analytics'),
    path('callback/', views.analytics, name='Callback'),
    path("<str:slug>", views.room, name="room"),
]
