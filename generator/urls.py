from django.urls import path
from .views import home, api_generar_contrasena

urlpatterns = [
    path('', home, name='home'),
    path('api/generar/', api_generar_contrasena, name='api_generar'),
]
