# product_service/products/serializers.py
from rest_framework import serializers
from .models import Menu, MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    """Serializer para los ítems del menú."""
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price']

class MenuSerializer(serializers.ModelSerializer):
    """Serializer para los menús, que incluye los ítems anidados."""
    # 'items' es el 'related_name' que definimos en el modelo MenuItem
    items = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ['id', 'name', 'commerce_id', 'items']