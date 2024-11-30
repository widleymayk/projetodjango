"""
URL configuration for projetodjango project.

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
from django.urls import path
from . import views  # Certifique-se de que views.py está no mesmo diretório

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adicionar_compromisso/', views.adicionar_compromisso, name='adicionar_compromisso'),
    path('visualizar_compromissos/', views.visualizar_compromissos, name='visualizar_compromissos'),
]



