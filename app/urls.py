from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.as_view(), name='feed'),
]

