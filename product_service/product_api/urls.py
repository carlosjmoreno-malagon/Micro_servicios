from django.contrib import admin
from django.urls import path, include

# Estas son las URLs de todo el microservicio
urlpatterns = [
    path('admin/', admin.site.urls),
    # Conecta todas las URLs de la app 'products' bajo el prefijo 'api/products/'
    path('api/products/', include('products.urls')),
]