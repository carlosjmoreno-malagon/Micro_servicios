# user_service/users/serializers.py

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """Serializer para crear y gestionar el perfil del propio usuario."""
    class Meta:
        model = User
        fields = ('email', 'password', 'name')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 5
            }
        }

    def create(self, validated_data):
        """Asegura que la contraseña se guarde hasheada."""
        return User.objects.create_user(**validated_data)

class UserDetailSerializer(serializers.ModelSerializer):
    """
    Serializer para mostrar los detalles PÚBLICOS de un usuario.
    No incluye la contraseña ni otros datos sensibles.
    """
    class Meta:
        model = User
        fields = ('id', 'email', 'name')