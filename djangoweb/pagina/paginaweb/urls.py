from django.contrib import admin
from django.urls import path
from paginaweb import views
from paginaweb.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('busqueda/', views.ingresar_usuario),
    path('registrar/', views.recuperar_contraseña),
]
   
