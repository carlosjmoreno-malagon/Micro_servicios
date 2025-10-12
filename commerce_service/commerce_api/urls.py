# commerce_service/commerce_api/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/commerces/', include('commerces.urls')),
]