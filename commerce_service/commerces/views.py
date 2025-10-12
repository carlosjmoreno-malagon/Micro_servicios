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
    # Solo los usuarios que presenten un token JWT válido podrán acceder.
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Sobrescribimos este método para asignar automáticamente el
        ID del usuario autenticado como el 'owner_id' del nuevo comercio.
        """
        # request.user.id está disponible gracias a que simplejwt decodificó
        # el token y nos dio el ID del usuario.
        serializer.save(owner_id=self.request.user.id)