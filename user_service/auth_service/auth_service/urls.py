# user_service/auth_service/urls.py

from django.contrib import admin
from django.urls import path, include

# Importamos la vista de login que nos da la librería
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),

    # =================== LOGIN ENDPOINT ===================
    # Aquí creamos la URL para el login.
    # Cualquier solicitud POST a '/api/token/' será manejada
    # por la vista TokenObtainPairView, que hace todo el trabajo.
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # ======================================================

    # También incluimos las URLs de registro que ya teníamos
    path('api/users/', include('users.urls')),
]