from django.db import models

class Menu(models.Model):
    """
    Representa una categoría de productos dentro de un comercio.
    Ejemplo: "Bebidas", "Pizzas", "Postres".
    """
    name = models.CharField(max_length=255)
    # Guarda una referencia numérica al ID del comercio del otro microservicio.
    commerce_id = models.IntegerField()

    def __str__(self):
        return f"{self.name} (Comercio ID: {self.commerce_id})"

class MenuItem(models.Model):
    """
    Representa un producto individual que se puede comprar.
    Ejemplo: "Coca-Cola", "Pizza Hawaiana".
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)  # Descripción opcional
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Relación directa con un Menú (viven en la misma base de datos).
    # Si se borra un menú, se borran todos sus productos.
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name