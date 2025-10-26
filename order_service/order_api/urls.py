# order_service/order_api/urls.py

from django.contrib import admin
from django.urls import path, include  # <-- Solo imports de Django

urlpatterns = [
    path('admin/', admin.site.urls),
    # Conecta las URLs de nuestra app 'orders' bajo el prefijo 'api/orders/'
    path('api/orders/', include('orders.urls')),
]