# commerce_service/commerces/models.py

from django.db import models

class Commerce(models.Model):
    """Modelo para representar un Comercio o Tienda."""
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    
    # --- ¡ESTA ES LA PARTE CLAVE! ---
    # No usamos una ForeignKey al modelo User porque no existe en esta BD.
    # Simplemente guardamos el ID del usuario (que viene del servicio de Auth)
    # como un número entero.
    owner_id = models.IntegerField()

    def __str__(self):
        return self.name