from django.urls import path
from django.shortcuts import render
from .views import UserListCreateView, UserDetailView



app_name = 'books'
urlpatterns = [
    # path('', index),
    path('user/list/', UserListCreateView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserDetailView.as_view()),
]