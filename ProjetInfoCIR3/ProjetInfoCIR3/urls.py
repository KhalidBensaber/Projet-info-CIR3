"""
URL configuration for ProjetInfoCIR3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from login import views as login_views  # Import the views from the login app
from django.contrib.auth import views as auth_views
from home import views as home_views
from home.views import react_app  # Importez votre vue React


"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_views.login, name='login'), # Default redirect to the login view in the login app
    path('login/', include('login.urls')),
    path('logout/', home_views.custom_logout, name='logout'), # Directs to the Django logout view
    path('home/', include('home.urls')),
    path('register/', include('register.urls')),
    path('telemetry/', include('telemetry.urls')),
    path('API/', include('testAPI.urls')),  # Add this line to include the testAPI app
]
    """
    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('TAPI/', include('testAPI.urls')),  # Garde les endpoints API existants
    path('', react_app, name='react'),  # Route par défaut (racine) pour React
    #re_path(r'^(?!API/).*$', react_app),
   
    path('api/login/', include('login.urls')),  # Inclure les routes API de l'app login
    path('api/register/', include('register.urls')),  # Inclure les routes API de l'app register
    path('logout/', home_views.custom_logout, name='logout'), # Directs to the Django logout view

    path('telemetry/', include('telemetry.urls')),

    
    ]
