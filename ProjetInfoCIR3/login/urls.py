from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.login, name='login'),
    path('', views.login, name='login_api'),  # Endpoint pour login
    path('logout/', views.logout, name='logout_api'),  # Endpoint pour logout
    path('check-auth/', views.check_auth, name='check_auth_api'),  # Vérification de l'authentification
    path('get-csrf-token/', views.get_csrf_token, name='get_csrf_token'),  # Récupération du token CSRF
    

]