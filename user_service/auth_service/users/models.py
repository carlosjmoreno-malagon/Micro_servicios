from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    """
    Manager para nuestro modelo de Usuario personalizado.
    """
    def create_user(self, email, password=None, **extra_fields):
        """Crea y guarda un nuevo usuario con el email y password dados."""
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        
        # Normaliza el email (convierte el dominio a minúsculas)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password) # Se encarga de hashear el password
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Crea y guarda un nuevo superusuario."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Modelo de Usuario personalizado que soporta login con email en lugar de username.
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # Permite acceder al admin de Django

    # Asignamos el Manager que creamos arriba
    objects = UserManager()

    # Usaremos el campo 'email' para el login
    USERNAME_FIELD = 'email'