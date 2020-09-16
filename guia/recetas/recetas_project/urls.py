"""recetas_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from recetas_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home',views.Home_view, name='Home'),
    path('Menú_Infantil', views.Menú_Infantil_view, name='Menú_Infantil'),
    path('Receta_Facil', views.Receta_Facil_view, name='Receta_Facil'),
    path('Mafe', views.Mafe_view, name='Mafe'),
    path('Feijoada', views.Feijoada_view, name='Feijoada'),
    path('Pizza', views.Pizza_view, name='Pizza'),
    path('Canelones', views.Canelones_view, name='Canelones'),
    path('Flor_de_Calabacin', views.Flor_de_Calabacin_view, name='Flor_de_Calabacin'),
    path('Gazpacho', views.Gazpacho_view, name='Gazpacho'),
    path('Sopa_de_Noodles', views.Sopa_de_Noodles_view, name='Sopa_de_Noodles'),
    path('Ensaladilla_Rusa', views.Ensaladilla_Rusa_view, name='Ensaladilla_Rusa'),
    path('Carbonara', views.Carbonara_view, name='Carbonara'),
]
