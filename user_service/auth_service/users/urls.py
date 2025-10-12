# user_service/users/urls.py

from django.urls import path
from .views import CreateUserView, ManageUserView, UserDetailView

app_name = 'users'

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('me/', ManageUserView.as_view(), name='me'),
    # NUEVA RUTA: Captura un número entero (int) desde la URL y lo pasa
    # a la vista como 'pk' (Primary Key).
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
]