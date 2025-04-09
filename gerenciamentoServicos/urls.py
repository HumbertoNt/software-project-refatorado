from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StatusEventoViewSet, EventoViewSet

routher = DefaultRouter()
routher.register('Status', StatusEventoViewSet)
routher.register('Eventos', EventoViewSet)

urlpatterns = [
    path('', include(routher.urls)),
]