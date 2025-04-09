"""
URL configuration for sistemaDeBiblioteca project.

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
from django.urls import path, include
from rest_framework import permissions 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger: documentação da API
schema_view = get_schema_view(
    openapi.Info(
        title='Sistema de Biblioteca API',
        default_version='v1',
        description='API para gerenciamento de biblioteca',
        #terms_of_service='',
        #contact=openapi.Contact(),
        #license=openapi.License(),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
        
# URL patterns serve para mapear as URLs para as views, lista de caminhos  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('gerenciamentoLivro/', include('gerenciamentoLivro.urls')),
    path('gerenciamentoUsuario/', include('gerenciamentoUsuario.urls')),
    path('gerenciamentoServicos/', include('gerenciamentoServicos.urls')),
]
