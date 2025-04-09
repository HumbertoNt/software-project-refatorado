from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StatusUsuarioViewSet, CadastrarUsuarioViewSet

routher = DefaultRouter()
routher.register('Status', StatusUsuarioViewSet)
routher.register('Novo Usuario', CadastrarUsuarioViewSet)

urlpatterns = [
    path('', include(routher.urls)),
]
