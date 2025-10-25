from django.urls import path
from .views import MenuListCreateView

# Estas son las URLs específicas de la app 'products'
urlpatterns = [
    # La ruta para listar y crear menús.
    path('menus/', MenuListCreateView.as_view(), name='menu-list-create'),
]