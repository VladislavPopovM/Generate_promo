from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.checker, name='checker'),
    # path('check/', views.check, name='check'),
]
