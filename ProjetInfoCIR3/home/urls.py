from django.urls import path, include, re_path
from . import views
from home.views import react_app  # Importez votre vue React
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('role_management/', views.role_management, name='role_management'),
    path('manage_matches/', views.manage_matches, name='manage_matches'),
    path('manage_events/', views.manage_events, name='manage_events'),
    path('manage_team/', views.manage_team, name='manage_team'),
    path('manage_accounts/', views.manage_accounts, name='manage_accounts'),
    path('donate/', views.donate, name='donate'),
    path('buy_ticket/', views.buy_ticket, name='buy_ticket'),
    path('get_ticket/', views.buy_ticket, name='get_ticket'),
    path('view_tickets/', views.view_tickets, name='view_tickets'),
    path('view_team_history/', views.view_team_history, name='view_team_history'),
    path('view_user_history/', views.view_user_history, name='view_user_history'),
]




