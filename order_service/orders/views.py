# order_service/orders/views.py

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer

class CartView(generics.GenericAPIView):
    """
    Vista para gestionar el carrito de compras de un usuario.
    GET: Devuelve el contenido del carrito del usuario actual.
    POST: Añade un producto al carrito del usuario actual.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartSerializer

    def get_object(self):
        """
        Obtiene o crea un carrito para el usuario autenticado.
        """
        # Usamos get_or_create para que, si el usuario nunca ha tenido un
        # carrito, se le cree uno automáticamente la primera vez.
        cart, created = Cart.objects.get_or_create(user_id=self.request.user.id)
        return cart

    def get(self, request, *args, **kwargs):
        """
        Maneja las solicitudes GET. Devuelve el carrito del usuario.
        """
        cart = self.get_object()
        serializer = self.get_serializer(cart)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        Maneja las solicitudes POST. Añade un ítem al carrito.
        """
        cart = self.get_object()
        
        # Esperamos que el body del POST contenga 'product_id' y 'quantity'.
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))

        if not product_id:
            return Response(
                {"error": "Product ID is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # TODO: En un futuro, aquí llamaremos al servicio de productos
        # para verificar que el product_id existe y está disponible.

        # Busca si el producto ya está en el carrito.
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product_id=product_id,
            defaults={'quantity': quantity}
        )

        # Si el ítem ya existía, simplemente actualizamos la cantidad.
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        
        # Devolvemos el estado actualizado del carrito completo.
        serializer = self.get_serializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)