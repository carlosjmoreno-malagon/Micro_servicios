# order_service/orders/serializers.py

from rest_framework import serializers
from .models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    """
    Serializer para los ítems dentro del carrito.
    """
    class Meta:
        model = CartItem
        # Solo necesitamos el ID del producto y la cantidad para la entrada.
        fields = ['id', 'product_id', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    """
    Serializer para el carrito de compras.
    Incluye una lista anidada de todos sus ítems.
    """
    # 'items' es el 'related_name' que definimos en el modelo CartItem.
    items = CartItemSerializer(many=True, read_only=True)
    
    # Campo extra para mostrar el total del carrito (solo lectura).
    total_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Cart
        fields = ['id', 'user_id', 'items', 'total_price', 'updated_at']

    def get_total_price(self, cart):
        # Este método calcula el precio total. Por ahora lo dejaremos en 0.
        # Más adelante, aquí haremos la llamada al servicio de productos.
        return 0.00