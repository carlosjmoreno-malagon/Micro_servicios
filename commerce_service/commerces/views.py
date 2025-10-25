# commerce_service/commerces/views.py

from rest_framework import generics, permissions
from .models import Commerce
from .serializers import CommerceSerializer

class CommerceListCreateView(generics.ListCreateAPIView):
    """
    Vista para listar todos los comercios y para crear uno nuevo.
    """
    queryset = Commerce.objects.all()
    serializer_class = CommerceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Asigna automáticamente el ID del usuario como el dueño del comercio."""
        serializer.save(owner_id=self.request.user.id)

# --- CÓDIGO A VERIFICAR / AÑADIR ---
class CommerceDetailView(generics.RetrieveAPIView):
    """
    Vista para obtener los detalles de un solo comercio por su ID.
    Este es el endpoint que el servicio de productos consultará.
    """
    queryset = Commerce.objects.all()
    serializer_class = CommerceSerializer
    permission_classes = [permissions.IsAuthenticated]