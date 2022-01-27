from django.urls import path, re_path
from django.contrib import admin
from . import views

app_name = 'chat'
urlpatterns = [
    path('', views.index, name='Index'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('user_auth', views.user_auth, name='user_auth'),
    path('user_logout', views.user_logout, name='user_logout'),
]
