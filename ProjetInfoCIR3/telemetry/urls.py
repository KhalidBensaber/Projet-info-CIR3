from django.urls import path
from . import views

urlpatterns = [
    path('', views.telemetry_dashboard, name='telemetry_dashboard'),
    path('api/', views.telemetry_api, name='telemetry_api'),
]
