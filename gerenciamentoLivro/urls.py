from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LivroViewSet, StatusLivroViewSet

routher = DefaultRouter()
routher.register('Livros', LivroViewSet)
routher.register('Status', StatusLivroViewSet)

urlpatterns = [
    path('', include(routher.urls)),
]
