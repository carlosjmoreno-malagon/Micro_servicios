# product_service/products/permissions.py

import requests
from rest_framework import permissions

class IsCommerceOwner(permissions.BasePermission):
    message = "You are not the owner of this commerce."

    def has_permission(self, request, view):
        if request.method != 'POST':
            return True

        commerce_id = request.data.get('commerce_id')
        if not commerce_id:
            self.message = "commerce_id must be provided in the request body."
            return False

        user_id_from_token = request.user.id # Esto podría ser string o int
        header = request.headers.get('Authorization')

        if not header:
            self.message = "Authorization header not found."
            return False
        
        try:
            url = f'http://127.0.0.1:8001/api/commerces/{commerce_id}/'
            headers_to_send = {'Authorization': header}
            response = requests.get(url, headers=headers_to_send, timeout=5)

            if response.status_code != 200:
                self.message = f"Could not verify commerce. Status code was {response.status_code}."
                return False

            commerce_data = response.json()
            owner_id_from_commerce = commerce_data.get('owner_id') # Esto es un int
            
            # --- LA CORRECCIÓN CLAVE ---
            # Nos aseguramos de comparar enteros con enteros.
            return int(owner_id_from_commerce) == int(user_id_from_token)

        except (requests.exceptions.RequestException, ValueError) as e:
            # ValueError capturará errores si los IDs no son números válidos
            print(f"ERROR: Fallo en la verificación. Error: {e}")
            self.message = "Could not verify ownership due to a connection or data error."
            return False