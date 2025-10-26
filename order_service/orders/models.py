# order_service/orders/models.py

from django.db import models

# --- MODELOS PARA EL CARRITO DE COMPRAS (TEMPORAL) ---

class Cart(models.Model):
    """
    Representa el carrito de compras de un usuario.
    Debería haber solo un carrito activo por usuario.
    """
    # ID del usuario del Servicio de Usuarios.
    user_id = models.IntegerField(unique=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart for User ID: {self.user_id}"

class CartItem(models.Model):
    """
    Representa un producto específico dentro de un carrito.
    """
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    # ID del producto del Servicio de Productos.
    product_id = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of Product ID {self.product_id} in Cart of User {self.cart.user_id}"

# --- MODELOS PARA EL PEDIDO (PERMANENTE) ---

class Order(models.Model):
    """
    Representa un pedido confirmado por un usuario.
    Es una "foto" inmutable de una compra en un momento dado.
    """
    class OrderStatus(models.TextChoices):
        PENDING = 'PENDING', 'Pendiente'
        PAID = 'PAID', 'Pagado'
        PROCESSING = 'PROCESSING', 'En Proceso'
        SHIPPED = 'SHIPPED', 'Enviado'
        DELIVERED = 'DELIVERED', 'Entregado'
        CANCELLED = 'CANCELLED', 'Cancelado'

    # ID del usuario que hizo el pedido.
    user_id = models.IntegerField()
    # ID del comercio al que se le pidió.
    commerce_id = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by User ID {self.user_id}"

class OrderItem(models.Model):
    """
    Representa un producto específico dentro de un pedido confirmado.
    Guarda los detalles del producto en el momento exacto de la compra.
    """
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    # ID del producto del Servicio de Productos.
    product_id = models.IntegerField()
    quantity = models.PositiveIntegerField()
    # ¡CRUCIAL! Guardamos el precio en el momento de la compra.
    # Esto evita que si el comercio cambia el precio mañana, el historial
    # de pedidos del usuario se vea alterado.
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)
    # También es una buena práctica guardar el nombre del producto.
    product_name_at_purchase = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.quantity} of {self.product_name_at_purchase}"