# commerce_service/commerces/urls.py
from django.urls import path
from .views import CommerceListCreateView

urlpatterns = [
    path('', CommerceListCreateView.as_view(), name='commerce-list-create'),
]