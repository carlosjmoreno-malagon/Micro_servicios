from rest_framework import generics, permissions
from .models import Menu
from .serializers import MenuSerializer
from .permissions import IsCommerceOwner  # Importamos nuestro permiso personalizado

class MenuListCreateView(generics.ListCreateAPIView):
    """
    Endpoint para:
    - Listar los menús de un comercio específico (GET).
    - Crear un nuevo menú para un comercio (POST).
    """
    serializer_class = MenuSerializer
    # Se aplican estos permisos a todas las solicitudes (GET y POST).
    # IsCommerceOwner solo restringirá el método POST, como lo definimos.
    permission_classes = [permissions.IsAuthenticated, IsCommerceOwner]

    def get_queryset(self):
        """
        Esta función filtra los resultados.
        Solo devuelve los menús que pertenecen al 'commerce_id' que se
        pasa como parámetro en la URL (ej: ?commerce_id=1).
        """
        commerce_id = self.request.query_params.get('commerce_id')
        if commerce_id:
            return Menu.objects.filter(commerce_id=commerce_id)
        # Si no se proporciona un commerce_id, no se devuelve ningún menú.
        return Menu.objects.none()

    def perform_create(self, serializer):
        """
        Esta función se ejecuta justo antes de guardar un nuevo menú.
        Asegura que el 'commerce_id' del cuerpo de la solicitud se guarde.
        """
        serializer.save(commerce_id=self.request.data.get('commerce_id'))