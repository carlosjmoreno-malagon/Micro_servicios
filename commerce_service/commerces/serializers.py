# commerce_service/commerces/serializers.py

from rest_framework import serializers
from .models import Commerce

class CommerceSerializer(serializers.ModelSerializer):
    """Serializer para el objeto Commerce."""

    class Meta:
        model = Commerce
        fields = ('id', 'name', 'address', 'phone', 'owner_id')
        # Hacemos que el owner_id sea de solo lectura.
        # No queremos que un usuario pueda asignar un comercio a otra persona.
        # Lo asignaremos automáticamente en la vista.
        read_only_fields = ('owner_id',)