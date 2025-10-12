# user_service/users/views.py

from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .serializers import UserSerializer, UserDetailSerializer

class CreateUserView(generics.CreateAPIView):
    """Crea un nuevo usuario en el sistema."""
    serializer_class = UserSerializer

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Vista para que un usuario vea y actualice su propio perfil."""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Devuelve el usuario autenticado."""
        return self.request.user

class UserDetailView(generics.RetrieveAPIView):
    """
    Vista para obtener los detalles públicos de un usuario por su ID.
    Esta es la vista que 'conecta' los microservicios.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]