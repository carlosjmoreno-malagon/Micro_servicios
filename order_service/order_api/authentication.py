# commerce_service/commerce_api/authentication.py

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.models import TokenUser

class StatelessJWTAuthentication(JWTAuthentication):
    """
    Clase de autenticación que valida un token JWT pero no intenta
    obtener el usuario de la base de datos local.

    Sobrescribe únicamente el método `get_user`.
    """
    def get_user(self, validated_token):
        """
        Evita el acceso a la base de datos. En su lugar, devuelve un
        objeto TokenUser ligero basado en el contenido del token validado.
        """
        return TokenUser(validated_token)