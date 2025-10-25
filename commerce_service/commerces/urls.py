# commerce_service/commerces/urls.py

from django.urls import path
from .views import CommerceListCreateView, CommerceDetailView # Importa ambas vistas

urlpatterns = [
    # Ruta para listar y crear: /api/commerces/
    path('', CommerceListCreateView.as_view(), name='commerce-list-create'),

    # --- CÓDIGO A VERIFICAR / AÑADIR ---
    # Ruta para obtener un comercio por su ID: /api/commerces/1/
    path('<int:pk>/', CommerceDetailView.as_view(), name='commerce-detail'),
]