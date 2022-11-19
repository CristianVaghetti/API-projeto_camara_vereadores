from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from vereador.api.viewsets import VereadorViewSet
from fornecedor.api.viewsets import FornecedorViewSet
from material.api.viewsets import MaterialViewSet
from utilizado.api.viewsets import UtilizadoViewSet

route = routers.DefaultRouter()
route.register(r'vereador', VereadorViewSet, basename='vereador')
route.register(r'fornecedor', FornecedorViewSet, basename='fornecedor')
route.register(r'material', MaterialViewSet, basename='material')
route.register(r'utilizar', UtilizadoViewSet, basename='utilizar')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]